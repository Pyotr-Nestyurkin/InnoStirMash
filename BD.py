from sqlalchemy import MetaData, create_engine
from datetime import datetime
import os

path1 = os.path.abspath(os.path.dirname('try_washer.sqlite'))

engine = create_engine('sqlite:///' + os.path.join(path1, 'try_washer.sqlite'))
metadata = MetaData()


def insert_into_table(tg_id, machine, time_h, time_m):
    connection = engine.connect()
    connection.execute(f"""INSERT OR REPLACE INTO z (id, machine_number, time_to_end_h, time_to_end_m)
    VALUES ({tg_id}, {machine}, {time_h}, {time_m})""")
    connection.close()


def m_n_computer(mn):
    connection = engine.connect()
    q = 0
    if mn == 1:
        spis1 = connection.execute(
            f"""SELECT machine_number FROM z WHERE machine_number = 11 or machine_number == 12""").fetchall()
        if spis1:
            spis = spis1[0]
            if len(spis) == 1:
                if spis[0] == 11:
                    q = 12
                elif spis[0] == 12:
                    q = 11
        else:
            q = 11
    elif mn == 2:
        spis2 = connection.execute(
            f"""SELECT machine_number FROM z WHERE machine_number = 21 or machine_number == 22""").fetchall()
        if spis2:
            spis = spis2[0]
            if len(spis) == 1:
                if spis[0] == 21:
                    q = 22
                elif spis[0] == 22:
                    q = 21
        else:
            q = 21
    elif mn == 3:
        spis3 = connection.execute(
            f"""SELECT machine_number FROM z WHERE machine_number = 31 or machine_number == 32""").fetchall()
        if spis3:
            spis = spis3[0]
            if len(spis) == 1:
                if spis[0] == 31:
                    q = 32
                elif spis[0] == 32:
                    q = 31
        else:
            q = 31
    connection.close()
    return (q)


def checker():
    t = [datetime.now().hour, datetime.now().minute]
    connection = engine.connect()
    sp = connection.execute(
        f"""SELECT id FROM z WHERE (time_to_end_h = {t[0]} and time_to_end_m = {t[1]})""").fetchone()
    sp1 = connection.execute(f"""SELECT machine_number FROM z 
    WHERE (time_to_end_h = {t[0]} and time_to_end_m = {t[1]})""").fetchone()
    connection.close()
    if sp:
        connection = engine.connect()
        connection.execute(
            f"""DELETE FROM z WHERE id = {sp[0]}""")
        connection.close()
        return [sp, sp1]
    else:
        return 0


def debtor_creator(id_d, machine_number_d):
    con = engine.connect()
    con.execute(f"""INSERT OR REPLACE INTO debtors (id, machine_number)
    VALUES ({id_d}, {machine_number_d})""")
    con.close()


def reporter(floor):
    con = engine.connect()
    zab = []
    if floor == 1:
        zab = con.execute(
            f"""SELECT id FROM debtors WHERE machine_number = 11 OR machine_number = 12 OR machine_number = 13""").fetchall()
    elif floor == 2:
        zab = con.execute(
            f"""SELECT id FROM debtors WHERE machine_number = 21 OR machine_number = 22 OR machine_number = 23""").fetchall()
    elif floor == 3:
        zab = con.execute(
            f"""SELECT id FROM debtors WHERE machine_number = 31 OR machine_number = 32 OR machine_number = 33""").fetchall()
    if len(zab) == 0:
        return 0
    else:
        return zab[0]


def debtor_forgiver(id_df):
    con = engine.connect()
    con.execute(f"""DELETE FROM debtors WHERE id = {id_df}""")
    con.close()


def machine_checker(floor):
    con_c = engine.connect()
    u = []
    if floor == 1:
        u = con_c.execute(
            f"""SELECT machine_number FROM z WHERE machine_number == 11 OR machine_number == 12 OR machine_number == 13""").fetchall()
    elif floor == 2:
        u = con_c.execute(
            f"""SELECT machine_number FROM z WHERE machine_number == 21 OR machine_number == 22 OR machine_number == 23""").fetchall()
    elif floor == 3:
        u = con_c.execute(
            f"""SELECT machine_number FROM z WHERE machine_number == 31 OR machine_number == 32 OR machine_number == 33""").fetchall()
    con_c.close()
    if len(u) > 0:
        return u[0]


def time_teller(m_n):
    con_t = engine.connect()
    ft = con_t.execute(
        f"""SELECT machine_number, time_to_end_h, time_to_end_m FROM z WHERE machine_number = {m_n}""").fetchall()
    con_t.close()
    return ft
