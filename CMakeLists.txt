cmake_minimum_required (VERSION 3.22)

project(StarkExDataAvailability VERSION 0.1.0)
include(CTest)

enable_testing()

if (NOT DEFINED CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

# Python library macro.
find_program(PYTHON "python3")

include("src/cmake_utils/cmake_rules.cmake")

add_subdirectory(src/starkware/committee)
add_subdirectory(src/starkware/crypto)
add_subdirectory(src/starkware/python)
add_subdirectory(src/starkware/starkware_utils)
add_subdirectory(src/starkware/storage)
add_subdirectory(src/services/perpetual)

# # Unit tests
# add_test (NAME python-tests
#   COMMAND ${PYTHON_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR}
#   WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/starkware
# )