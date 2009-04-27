int countchar(const char* str, char ch) {
    int res = 0;
    while (*str) {
        if (*str == ch) ++res;
        ++str;
    }
    return res;
}

