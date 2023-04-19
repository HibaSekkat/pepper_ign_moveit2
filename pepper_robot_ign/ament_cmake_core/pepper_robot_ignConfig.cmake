# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_pepper_robot_ign_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED pepper_robot_ign_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(pepper_robot_ign_FOUND FALSE)
  elseif(NOT pepper_robot_ign_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(pepper_robot_ign_FOUND FALSE)
  endif()
  return()
endif()
set(_pepper_robot_ign_CONFIG_INCLUDED TRUE)

# output package information
if(NOT pepper_robot_ign_FIND_QUIETLY)
  message(STATUS "Found pepper_robot_ign: 1.0.0 (${pepper_robot_ign_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'pepper_robot_ign' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${pepper_robot_ign_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(pepper_robot_ign_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${pepper_robot_ign_DIR}/${_extra}")
endforeach()
