from __future__ import absolute_import
from .ffi import FFI

class EndianTranlation(object):
    _endian = None
    _ntoh = _hton = None


    def loadendian_translate(self, ffi=None):
        import platform

        ffi = FFI()

        if None in (EndianTranlation._endian, EndianTranlation._ntoh, EndianTranlation._hton):
            ffi.cdef("""
            uint32_t htonl(uint32_t hostlong);
            uint16_t htons(uint16_t hostshort);
            uint32_t ntohl(uint32_t netlong);
            uint16_t ntohs(uint16_t netshort);
            """, override=True)

            if platform.system() == 'Windows':
                ffi.cdef("""
                uint64_t htonll(uint64_t hostlong);
                uint64_t ntohll(uint64_t netlong);
                uint32_t htonf(float hostfloat);
                float ntohf(uint32_t netfloat);
                uint64_t htond(double hostdouble);
                double ntohd(uint64_t netdouble);
                """, override=True)

                EndianTranlation._endian = ffi.dlopen("Ws2_32")

            else:
                raise NotImplementedError()

            _endian = EndianTranlation._endian
            
            EndianTranlation._ntoh = dict(
                int16_t=_endian.ntohs,
                uint16_t=_endian.ntohs,
                int32_t=_endian.ntohl,
                uint32_t=_endian.ntohl,
                int64_t=lambda x: (_endian.ntohl(x & 0xFFFFFFFF) << 32) | _endian.ntohl(x >> 32),
                uint64_t=lambda x: (_endian.ntohl(x & 0xFFFFFFFF) << 32) | _endian.ntohl(x >> 32),
                # float    = _endian.ntohf,
                # double   = _endian.ntohd,
            )
            EndianTranlation._hton = dict(
                int16_t=_endian.htons,
                uint16_t=_endian.htons,
                int32_t=_endian.htonl,
                uint32_t=_endian.htonl,
                int64_t=lambda x: (_endian.htonl(x & 0xFFFFFFFF) << 32) | _endian.htonl(x >> 32),
                uint64_t=lambda x: (_endian.htonl(x & 0xFFFFFFFF) << 32) | _endian.htonl(x >> 32),
                # float    = self._endian.htonf,
                # double   = self._endian.htond,
            )

    @property
    def ntoh(self):
        return EndianTranlation._ntoh

    @property
    def hton(self):
        return EndianTranlation._hton
