disketa_bait = 1.44 * 1024 * 1024
stranici = 100
stroki_na_stranice = 50
simvoli_v_stroke = 25
simv_v_knige = stranici * stroki_na_stranice * simvoli_v_stroke
ves_knigi = simv_v_knige * 4

kolichestvo_knig = int(disketa_bait/ves_knigi)

print("Количество книг, помещающихся на дискету:", kolichestvo_knig)
