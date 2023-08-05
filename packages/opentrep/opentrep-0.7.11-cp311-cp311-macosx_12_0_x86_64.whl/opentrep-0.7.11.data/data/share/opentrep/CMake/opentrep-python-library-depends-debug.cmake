#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "pyopentreplib" for configuration "Debug"
set_property(TARGET pyopentreplib APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(pyopentreplib PROPERTIES
  IMPORTED_LOCATION_DEBUG "/Users/DENIS/dev/geo/opentrep/_skbuild/macosx-12.0-x86_64-3.11/cmake-install/lib/python3.11/site-packages/pyopentrep/pyopentrep.0.07.12.so"
  IMPORTED_SONAME_DEBUG "@rpath/pyopentrep.0.07.so"
  )

list(APPEND _cmake_import_check_targets pyopentreplib )
list(APPEND _cmake_import_check_files_for_pyopentreplib "/Users/DENIS/dev/geo/opentrep/_skbuild/macosx-12.0-x86_64-3.11/cmake-install/lib/python3.11/site-packages/pyopentrep/pyopentrep.0.07.12.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
