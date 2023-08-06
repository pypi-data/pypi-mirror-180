
#ifndef RSERRORS_EXPORT_H
#define RSERRORS_EXPORT_H

#ifdef RSERRORS_STATIC_DEFINE
#  define RSERRORS_EXPORT
#  define RSERRORS_NO_EXPORT
#else
#  ifndef RSERRORS_EXPORT
#    ifdef rserrors_EXPORTS
        /* We are building this library */
#      define RSERRORS_EXPORT 
#    else
        /* We are using this library */
#      define RSERRORS_EXPORT 
#    endif
#  endif

#  ifndef RSERRORS_NO_EXPORT
#    define RSERRORS_NO_EXPORT 
#  endif
#endif

#ifndef RSERRORS_DEPRECATED
#  define RSERRORS_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef RSERRORS_DEPRECATED_EXPORT
#  define RSERRORS_DEPRECATED_EXPORT RSERRORS_EXPORT RSERRORS_DEPRECATED
#endif

#ifndef RSERRORS_DEPRECATED_NO_EXPORT
#  define RSERRORS_DEPRECATED_NO_EXPORT RSERRORS_NO_EXPORT RSERRORS_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef RSERRORS_NO_DEPRECATED
#    define RSERRORS_NO_DEPRECATED
#  endif
#endif

#endif /* RSERRORS_EXPORT_H */
