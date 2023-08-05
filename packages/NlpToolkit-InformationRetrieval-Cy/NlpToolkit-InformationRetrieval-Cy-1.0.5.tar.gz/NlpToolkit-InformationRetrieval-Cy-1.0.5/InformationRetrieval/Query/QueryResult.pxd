cdef class QueryResult:

    cdef list __items

    cpdef add(self, int docId, float score = *)
    cpdef list getItems(self)
    cpdef int size(self)
    cpdef QueryResult intersection(self, QueryResult queryResult)
