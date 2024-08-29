from tests import config as config


def get_breed_data():
    SELECT_DATA = """select breeds.TEXT_PARTNER_BREED_CODE, breeds.TEXT_PARTNER_BREED_DESC, colors.TEXT_PARTNER_COLOR_CODE
                from AKC.T_PARTNER_BREED_DATA_AKC breeds, AKC.T_PARTNER_BREED_COLORS_AKC colors
                where breeds.KEY_PARTNER_BREED = colors.KEY_PARTNER_BREED order by breeds.TEXT_PARTNER_BREED_CODE"""

    breed_code = 0
    ckc_breed = 0
    ckc_color = 0
    con = config.get_edb_conn()
    cur = con.cursor()
    cur.execute(SELECT_DATA)

    for values in cur:
        breed_code = values[0]
        ckc_breed = values[1]
        ckc_color = values[2]
        break

    cur.close()
    con.close()
    return breed_code, ckc_breed, ckc_color

