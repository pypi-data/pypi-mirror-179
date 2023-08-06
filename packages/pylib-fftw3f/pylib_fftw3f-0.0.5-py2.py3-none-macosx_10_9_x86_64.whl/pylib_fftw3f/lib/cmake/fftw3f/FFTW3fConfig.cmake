# defined since 2.8.3
if (CMAKE_VERSION VERSION_LESS 2.8.3)
  get_filename_component (CMAKE_CURRENT_LIST_DIR ${CMAKE_CURRENT_LIST_FILE} PATH)
endif ()

# Allows loading FFTW3 settings from another project
set (FFTW3_CONFIG_FILE "${CMAKE_CURRENT_LIST_FILE}")

set (FFTW3f_LIBRARIES fftw3f)
set (FFTW3f_LIBRARY_DIRS /Users/runner/work/pylib-fftw3f/pylib-fftw3f/build/lib.macosx-10.9-x86_64-3.6/pylib_fftw3f/lib)
set (FFTW3f_INCLUDE_DIRS /Users/runner/work/pylib-fftw3f/pylib-fftw3f/build/lib.macosx-10.9-x86_64-3.6/pylib_fftw3f/include)

include ("${CMAKE_CURRENT_LIST_DIR}/FFTW3LibraryDepends.cmake")

if (CMAKE_VERSION VERSION_LESS 2.8.3)
  set (CMAKE_CURRENT_LIST_DIR)
endif ()
