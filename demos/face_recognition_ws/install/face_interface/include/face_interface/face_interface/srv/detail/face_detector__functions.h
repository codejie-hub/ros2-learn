// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from face_interface:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef FACE_INTERFACE__SRV__DETAIL__FACE_DETECTOR__FUNCTIONS_H_
#define FACE_INTERFACE__SRV__DETAIL__FACE_DETECTOR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "face_interface/msg/rosidl_generator_c__visibility_control.h"

#include "face_interface/srv/detail/face_detector__struct.h"

/// Initialize srv/FaceDetector message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * face_interface__srv__FaceDetector_Request
 * )) before or use
 * face_interface__srv__FaceDetector_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__init(face_interface__srv__FaceDetector_Request * msg);

/// Finalize srv/FaceDetector message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Request__fini(face_interface__srv__FaceDetector_Request * msg);

/// Create srv/FaceDetector message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * face_interface__srv__FaceDetector_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
face_interface__srv__FaceDetector_Request *
face_interface__srv__FaceDetector_Request__create();

/// Destroy srv/FaceDetector message.
/**
 * It calls
 * face_interface__srv__FaceDetector_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Request__destroy(face_interface__srv__FaceDetector_Request * msg);

/// Check for srv/FaceDetector message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__are_equal(const face_interface__srv__FaceDetector_Request * lhs, const face_interface__srv__FaceDetector_Request * rhs);

/// Copy a srv/FaceDetector message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__copy(
  const face_interface__srv__FaceDetector_Request * input,
  face_interface__srv__FaceDetector_Request * output);

/// Initialize array of srv/FaceDetector messages.
/**
 * It allocates the memory for the number of elements and calls
 * face_interface__srv__FaceDetector_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__Sequence__init(face_interface__srv__FaceDetector_Request__Sequence * array, size_t size);

/// Finalize array of srv/FaceDetector messages.
/**
 * It calls
 * face_interface__srv__FaceDetector_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Request__Sequence__fini(face_interface__srv__FaceDetector_Request__Sequence * array);

/// Create array of srv/FaceDetector messages.
/**
 * It allocates the memory for the array and calls
 * face_interface__srv__FaceDetector_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
face_interface__srv__FaceDetector_Request__Sequence *
face_interface__srv__FaceDetector_Request__Sequence__create(size_t size);

/// Destroy array of srv/FaceDetector messages.
/**
 * It calls
 * face_interface__srv__FaceDetector_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Request__Sequence__destroy(face_interface__srv__FaceDetector_Request__Sequence * array);

/// Check for srv/FaceDetector message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__Sequence__are_equal(const face_interface__srv__FaceDetector_Request__Sequence * lhs, const face_interface__srv__FaceDetector_Request__Sequence * rhs);

/// Copy an array of srv/FaceDetector messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Request__Sequence__copy(
  const face_interface__srv__FaceDetector_Request__Sequence * input,
  face_interface__srv__FaceDetector_Request__Sequence * output);

/// Initialize srv/FaceDetector message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * face_interface__srv__FaceDetector_Response
 * )) before or use
 * face_interface__srv__FaceDetector_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__init(face_interface__srv__FaceDetector_Response * msg);

/// Finalize srv/FaceDetector message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Response__fini(face_interface__srv__FaceDetector_Response * msg);

/// Create srv/FaceDetector message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * face_interface__srv__FaceDetector_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
face_interface__srv__FaceDetector_Response *
face_interface__srv__FaceDetector_Response__create();

/// Destroy srv/FaceDetector message.
/**
 * It calls
 * face_interface__srv__FaceDetector_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Response__destroy(face_interface__srv__FaceDetector_Response * msg);

/// Check for srv/FaceDetector message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__are_equal(const face_interface__srv__FaceDetector_Response * lhs, const face_interface__srv__FaceDetector_Response * rhs);

/// Copy a srv/FaceDetector message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__copy(
  const face_interface__srv__FaceDetector_Response * input,
  face_interface__srv__FaceDetector_Response * output);

/// Initialize array of srv/FaceDetector messages.
/**
 * It allocates the memory for the number of elements and calls
 * face_interface__srv__FaceDetector_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__Sequence__init(face_interface__srv__FaceDetector_Response__Sequence * array, size_t size);

/// Finalize array of srv/FaceDetector messages.
/**
 * It calls
 * face_interface__srv__FaceDetector_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Response__Sequence__fini(face_interface__srv__FaceDetector_Response__Sequence * array);

/// Create array of srv/FaceDetector messages.
/**
 * It allocates the memory for the array and calls
 * face_interface__srv__FaceDetector_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
face_interface__srv__FaceDetector_Response__Sequence *
face_interface__srv__FaceDetector_Response__Sequence__create(size_t size);

/// Destroy array of srv/FaceDetector messages.
/**
 * It calls
 * face_interface__srv__FaceDetector_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
void
face_interface__srv__FaceDetector_Response__Sequence__destroy(face_interface__srv__FaceDetector_Response__Sequence * array);

/// Check for srv/FaceDetector message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__Sequence__are_equal(const face_interface__srv__FaceDetector_Response__Sequence * lhs, const face_interface__srv__FaceDetector_Response__Sequence * rhs);

/// Copy an array of srv/FaceDetector messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_face_interface
bool
face_interface__srv__FaceDetector_Response__Sequence__copy(
  const face_interface__srv__FaceDetector_Response__Sequence * input,
  face_interface__srv__FaceDetector_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FACE_INTERFACE__SRV__DETAIL__FACE_DETECTOR__FUNCTIONS_H_
