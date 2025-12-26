#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <mcl/bls12_381.hpp>

namespace py = pybind11;

// Use the BLS12-381 namespace provided by mcl
using namespace mcl::bls12;

// Buffer sizes for serialization
constexpr std::size_t kFrBufSize =  32;
constexpr std::size_t kG1BufSize =  48;
constexpr std::size_t kG2BufSize =  96;
constexpr std::size_t kGTBufSize = 576;

// -----------------------------------------------------------------------------
// Helper Functions
// -----------------------------------------------------------------------------

// Generic string representation wrapper
template<typename T>
std::string to_string_obj(T const &obj) {
    return obj.getStr(10);  // 10 for decimal
}

// Generic hash function for Python's __hash__
// Hashes the serialized bytes of the object
template<typename T, size_t bufSize>
size_t python_hash_obj(T const &obj) {
    char buf[bufSize];
    size_t n = obj.serialize(buf, bufSize);
    std::string_view view(buf, n);
    return std::hash<std::string_view>{}(view);
}

// Generic serialization wrapper
template<typename T, size_t bufSize>
py::bytes serialize_obj(T const &obj) {
    char buf[bufSize];
    size_t n = obj.serialize(buf, bufSize);
    if (n == 0) {
        throw std::runtime_error("Serialization failed");
    }
    return py::bytes(buf, n);
}

// Generic deserialization wrapper (Factory method)
template<typename T>
T deserialize_obj(std::string_view sv) {
    T obj;
    if (obj.deserialize(sv.data(), sv.size()) == 0) {
        throw std::invalid_argument("Could not deserialize bytes");
    }
    return obj;
}

// -----------------------------------------------------------------------------
// Module Definition
// -----------------------------------------------------------------------------

PYBIND11_MODULE(_pymcl, m) {
    m.doc() = "A Python 3 wrapper for the mcl library (BLS12-381) using Pybind11.";

    // Initialize mcl library for BLS12-381
    // This runs when the module is imported
    mcl::initPairing(mcl::BLS12_381);

    // -------------------------------------------------------------------------
    // Fr Class
    // -------------------------------------------------------------------------
    py::class_<Fr>(m, "Fr")
        .def(py::init([]() {
            Fr fr;
            fr.clear();
            return fr;
        }))
        .def(py::init([](std::string const &s, int base) {
            Fr fr;
            fr.setStr(s, base);
            return fr;
        }), py::arg("s"), py::arg("base") = 0)
        .def(py::init([](int64_t v) {
            Fr fr;
            fr = v;
            return fr;
        }))

        // Utilities
        .def_static("random", []() {
            Fr fr;
            fr.setByCSPRNG();
            return fr;
        }, "Generates a random Fr element.")

        // Serialization / String
        .def("__str__", &to_string_obj<Fr>)
        .def("__repr__", [](Fr const &self) {
            return "<Fr " + to_string_obj<Fr>(self) + ">";
        })
        .def("__hash__", &python_hash_obj<Fr, kFrBufSize>)
        .def("serialize", &serialize_obj<Fr, kFrBufSize>, "Serializes the element to a byte string.")
        .def_static("deserialize", &deserialize_obj<Fr>, "Deserializes the element from a byte string.")

        // Utilities
        .def("is_zero", &Fr::isZero)
        .def("is_one", &Fr::isOne)

        // Deprecated utilities
        .def("isZero", &Fr::isZero)
        .def("isOne", &Fr::isOne)

        // Comparison
        .def(py::self == py::self)
        .def(py::self != py::self)

        // Arithmetic Operators
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(-py::self)
        .def(py::self * py::self)
        .def(py::self / py::self)
        .def("__invert__", [](Fr const &self) {
            Fr res;
            Fr::inv(res, self);
            return res;
        });

    // -------------------------------------------------------------------------
    // G1 Class
    // -------------------------------------------------------------------------
    py::class_<G1>(m, "G1")
        .def(py::init([]() {
            G1 g1;
            g1.clear();
            return g1;
        }))
        .def(py::init([](std::string const &s, int mode) {
            G1 g1;
            g1.setStr(s, mode);
            return g1;
        }), py::arg("s"), py::arg("mode") = 0)

        // Hash to Curve
        .def_static("hash", [](std::string_view sv) {
            G1 g1;
            hashAndMapToG1(g1, sv.data(), sv.size());
            return g1;
        }, "Hashes a byte string to a G1 element.")

        // Serialization / String
        .def("__str__", &to_string_obj<G1>)
        .def("__repr__", [](G1 const &self) {
            return "<G1 " + to_string_obj<G1>(self) + ">";
        })
        .def("__hash__", &python_hash_obj<G1, kG1BufSize>)
        .def("serialize", &serialize_obj<G1, kG1BufSize>)
        .def_static("deserialize", &deserialize_obj<G1>)

        // Utilities
        .def("is_zero", &G1::isZero)

        // Deprecated utilities
        .def("isZero", &G1::isZero)

        // Comparison
        .def(py::self == py::self)
        .def(py::self != py::self)

        // Arithmetic
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(-py::self)

        // G1 * Fr (Scalar Multiplication)
        .def("__mul__", [](G1 const &self, Fr const &other) {
            return self * other;
        });

    // -------------------------------------------------------------------------
    // G2 Class
    // -------------------------------------------------------------------------
    py::class_<G2>(m, "G2")
        .def(py::init([]() {
            G2 g2;
            g2.clear();
            return g2;
        }))
        .def(py::init([](std::string const &s, int mode) {
            G2 g2;
            g2.setStr(s, mode);
            return g2;
        }), py::arg("s"), py::arg("mode") = 0)

        // Hash to Curve
        .def_static("hash", [](std::string_view sv) {
            G2 g2;
            hashAndMapToG2(g2, sv.data(), sv.size());
            return g2;
        }, "Hashes a byte string to a G2 element.")

        // Serialization / String
        .def("__str__", &to_string_obj<G2>)
        .def("__repr__", [](G2 const &self) {
            return "<G2 " + to_string_obj<G2>(self) + ">";
        })
        .def("__hash__", &python_hash_obj<G2, kG2BufSize>)
        .def("serialize", &serialize_obj<G2, kG2BufSize>)
        .def_static("deserialize", &deserialize_obj<G2>)

        // Utilities
        .def("is_zero", &G2::isZero)

        // Deprecated utilities
        .def("isZero", &G2::isZero)

        // Comparison
        .def(py::self == py::self)
        .def(py::self != py::self)

        // Arithmetic
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(-py::self)

        // G2 * Fr (Scalar Multiplication)
        .def("__mul__", [](G2 const &self, Fr const &other) {
            return self * other;
        });

    // -------------------------------------------------------------------------
    // GT Class
    // -------------------------------------------------------------------------
    py::class_<GT>(m, "GT")
        .def(py::init([](py::bool_ one) {
            GT gt;
            one ? gt.setOne() : gt.clear();
            return gt;
        }), py::arg("one") = true)
        .def(py::init([](std::string const &s, int mode) {
            GT gt;
            gt.setStr(s, mode);
            return gt;
        }), py::arg("s"), py::arg("mode") = 0)

        // Serialization / String
        .def("__str__", &to_string_obj<GT>)
        .def("__repr__", [](GT const &self) {
            return "<GT " + to_string_obj<GT>(self) + ">";
        })
        .def("__hash__", &python_hash_obj<GT, kGTBufSize>)
        .def("serialize", &serialize_obj<GT, kGTBufSize>)
        .def_static("deserialize", &deserialize_obj<GT>)

        // Utilities
        .def("is_zero", &GT::isZero)
        .def("is_one", &GT::isOne)

        // Deprecated utilities
        .def("isZero", &GT::isZero)
        .def("isOne", &GT::isOne)

        // Comparison
        .def(py::self == py::self)
        .def(py::self != py::self)

        // Arithmetic (GT is a multiplicative group)
        .def(py::self * py::self)
        .def(py::self / py::self)
        .def("__invert__", [](GT const &self) {
            GT res;
            GT::inv(res, self);
            return res;
        })

        // GT ** Fr (Exponentiation)
        .def("__pow__", [](GT const &self, Fr const &exp) {
            GT res;
            GT::pow(res, self, exp);
            return res;
        });

    // -------------------------------------------------------------------------
    // Pairing Function
    // -------------------------------------------------------------------------
    m.def("pairing", [](G1 const &P, G2 const &Q) {
        GT res;
        pairing(res, P, Q);
        return res;
    }, "Computes the pairing between a G1 and a G2 element.");

    // -------------------------------------------------------------------------
    // Constants
    // -------------------------------------------------------------------------

    // r (Curve Order)
    char const *rStr = "0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001";
    m.attr("r") = py::reinterpret_steal<py::object>(PyLong_FromString(rStr, nullptr, 0));

    // g1 (Generator)
    char const *g1Str = "1 0x17f1d3a73197d7942695638c4fa9ac0fc3688c4f9774b905a14e3a3f171bac586c55e83ff97a1aeffb3af00adb22c6bb 0x08b3f481e3aaa0f1a09e30ed741d8ae4fcf5e095d5d00af600db18cb2c04b3edd03cc744a2888ae40caa232946c5e7e1";
    G1 g1_const;
    g1_const.setStr(g1Str, 16);
    m.attr("g1") = g1_const;

    // g2 (Generator)
    char const *g2Str = "1 0x24aa2b2f08f0a91260805272dc51051c6e47ad4fa403b02b4510b647ae3d1770bac0326a805bbefd48056c8c121bdb8 0x13e02b6052719f607dacd3a088274f65596bd0d09920b61ab5da61bbdc7f5049334cf11213945d57e5ac7d055d042b7e 0x0ce5d527727d6e118cc9cdc6da2e351aadfd9baa8cbdd3a76d429a695160d12c923ac9cc3baca289e193548608b82801 0x0606c4a02ea734cc32acd2b02bc28b99cb3e287e85a763af267492ab572e99ab3f370d275cec1da1aaa9075ff05f79be";
    G2 g2_const;
    g2_const.setStr(g2Str, 16);
    m.attr("g2") = g2_const;
}
