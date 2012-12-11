#include <stdint.h>
#include <stdbool.h>

typedef unsigned char boolean;

typedef /*@signed-integral-type@*/ int8_t       sint8;
typedef /*@unsigned-integral-type@*/ uint8_t    uint8;
typedef /*@signed-integral-type@*/ int16_t      sint16;
typedef /*@unsigned-integral-type@*/ uint16_t   uint16;
typedef /*@signed-integral-type@*/ int32_t      sint32;
typedef /*@unsigned-integral-type@*/ uint32_t   uint32;

typedef /*@signed-integral-type@*/ int_least8_t     sint8_least;
typedef /*@unsigned-integral-type@*/ uint_least8_t  uint8_least;
typedef /*@signed-integral-type@*/ int_least16_t    sint16_least;
typedef /*@unsigned-integral-type@*/ uint_least16_t uint16_least;
typedef /*@signed-integral-type@*/ int_least32_t    sint32_least;
typedef /*@unsigned-integral-type@*/ uint_least32_t uint32_least;
