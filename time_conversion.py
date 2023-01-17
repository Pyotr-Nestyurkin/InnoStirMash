from BD import insert_into_table


def white(user_id, machine_number, st_time):  # + час
    if st_time[0] != 23:
        st_time[0] += 1
    else:
        st_time[0] = 0
    insert_into_table(user_id, machine_number, st_time[0], st_time[1])


def fast_st(user_id, machine_number, st_time):  # + полчаса
    if st_time[1] < 30:
        st_time[1] += 30
    else:
        if st_time[0] != 23:
            st_time[0] += 1
            st_time[1] -= 30
        elif st_time[0] == 23:
            st_time[0] = 0

    insert_into_table(user_id, machine_number, st_time[0], st_time[1])


def dry(user_id, machine_number, st_time):  # + 2 часа
    # if st_time[0] != 22:
    #     st_time[0] += 2
    # else:
    #    st_time[0] = 0
    pass
    insert_into_table(user_id, machine_number, st_time[0], st_time[1])