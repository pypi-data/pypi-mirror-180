
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.10.0
)
FetchContent_MakeAvailable(pybind11 relic)

pybind11_add_module(chinillablspy ${CMAKE_CURRENT_SOURCE_DIR}/pythonbindings.cpp)
target_link_libraries(chinillablspy PRIVATE bls)
