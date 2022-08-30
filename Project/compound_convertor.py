def compoundConverter(compound_string):
    compound_name = ""
    compound_num = ""
    compound_string += "E"

    str_list = []

    for s in compound_string:
        run = False
        if s == '(' or s == ')':
            run = True

        if ord('0') <= ord(s) and ord(s) <= ord('9'):
            compound_num += s
        else:
            if (s.upper() == s and (compound_name != "" or compound_num != "")) or run:
                if compound_name == "" and compound_num != "":
                    str_list.append([compound_num, 1])
                    compound_num = ""

                if compound_num != "":
                    # st.append([compound_name, int(compound_num)])
                    str_list.append([compound_name, 0])
                    str_list.append([compound_num, 1])
                elif compound_name != "":
                    # st.append([compound_name, 1])
                    str_list.append([compound_name, 0])
                    str_list.append(['1', 1])

                if not run:
                    compound_name = s
                    compound_num = ""
                else:
                    str_list.append([s, 2])
                    compound_name = ""
                    compound_num = ""
            else:
                compound_name += s

    if compound_num != "":
        str_list.append([compound_num, 1])

    st = []

    for elem in str_list:
        if elem[1] == 0:
            st.append([elem[0], 1])
        elif elem[1] == 1:
            if st[-1] == ')':
                st.pop()
                tmp_st = []
                while st[-1] != '(':
                    st_top = st[-1]
                    st.pop()
                    st_top[1] *= int(elem[0])
                    tmp_st.append(st_top)

                st.pop()
                for x in tmp_st:
                    st.append(x)
            else:
                st_top = st[-1]
                st.pop()
                st_top[1] *= int(elem[0])
                st.append(st_top)
        else:
            st.append(elem[0])

    st.sort()

    for i in range(1, len(st)):
        if st[-i][0] == st[-(i + 1)][0]:
            st[-(i + 1)][1] += st[-i][1]
            st[-i][1] = 0

    ans = []
    for x in st:
        if x[1] != 0:
            ans.append(x)
    return ans
