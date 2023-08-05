/*
    Copyright (c) 2022 Advanced Micro Devices, Inc. All rights reserved.
*/

#ifndef ROCM_SYMLINK_ROCSPARSE_TYPES_H
#define ROCM_SYMLINK_ROCSPARSE_TYPES_H

#if defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING)
/* include file */
#include "rocsparse/rocsparse-types.h"
#else
/* give warning */
#if defined(_MSC_VER)
#pragma message(": warning:This file is deprecated. Use the header file from /opt/rocm-5.4.0/include/rocsparse/rocsparse-types.h by using #include <rocsparse/rocsparse-types.h>")
#elif defined(__GNUC__)
#pragma message(": warning : This file is deprecated. Use the header file from /opt/rocm-5.4.0/include/rocsparse/rocsparse-types.h by using #include <rocsparse/rocsparse-types.h>")
#endif
/* include file */
#define ROCM_SYMLINK_GAVE_WARNING
#include "rocsparse/rocsparse-types.h"
#undef ROCM_SYMLINK_GAVE_WARNING
#endif /* defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING) */

#endif /* ROCM_SYMLINK_ROCSPARSE_TYPES_H */


