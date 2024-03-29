from ingidients_calculator import IngridientsCalculator

puzzle_input = """13 WDSR, 16 FXQB => 6 BSTCB
185 ORE => 9 BWSCM
1 WDSR => 9 RLFSK
5 LCGL, 7 BWSCM => 9 BSVW
6 NLSL => 3 MJSQ
1 JFGM, 7 BSVW, 7 XRLN => 6 WDSR
3 WZLFV => 3 BZDPT
5 DTHZH, 12 QNTH, 20 BSTCB => 4 BMXF
18 JSJWJ, 6 JLMD, 6 TMTF, 3 XSNL, 3 BWSCM, 83 LQTJ, 29 KDGNL => 1 FUEL
1 LWPD, 28 RTML, 16 FDPM, 8 JSJWJ, 2 TNMTC, 20 DTHZH => 9 JLMD
1 SDVXW => 6 BPTV
180 ORE => 7 JFGM
13 RLFSK, 15 HRKD, 1 RFQWL => 5 QNTH
1 RFQWL, 3 NZHFV, 18 XRLN => 9 HRKD
2 NLSL, 2 JXVZ => 5 GTSJ
19 SDVXW, 2 BSVW, 19 XRLN => 6 QMFV
1 CSKP => 8 LQTJ
4 ZSZBN => 5 RBRZT
8 WZLFV, 3 QNWRZ, 1 DTHZH => 4 RTRN
1 CGXBG, 1 PGXFJ => 3 TNMTC
4 CGCSL => 7 RNFW
9 CGCSL, 1 HGTL, 3 BHJXV => 8 RSVR
5 NGJW => 8 HTDM
21 FPBTN, 1 TNMTC, 2 RBRZT, 8 BDHJ, 28 WXQX, 9 RNFW, 6 RSVR => 1 XSNL
2 WZLFV => 5 BHJXV
10 BSTCB, 4 NLSL => 4 HQLHN
1 JFGM => 7 SDVXW
6 CSKP => 8 FXQB
6 TNMTC, 4 BZDPT, 1 BPTV, 18 JSJWJ, 2 DTHZH, 1 LWPD, 8 RTML => 8 KDGNL
6 XFGWZ => 7 CGCSL
3 GTSJ => 4 LWPD
1 WDSR, 1 QNWRZ => 5 XFGWZ
11 CSKP, 10 SDVXW => 4 QNWRZ
7 BSVW, 4 QMFV => 1 RFQWL
12 QNTH, 10 HTDM, 3 WXQX => 3 FDPM
2 HGTL => 7 PGXFJ
14 SDVXW => 6 CSKP
11 HQLHN, 1 GTSJ, 1 QNTH => 5 TMTF
173 ORE => 9 LCGL
4 WXQX => 9 BDHJ
5 BZDPT => 7 NGJW
1 GTSJ, 23 QNWRZ, 6 LQTJ => 7 JSJWJ
23 NZHFV, 3 HQLHN => 6 DTHZH
2 JFGM => 4 XRLN
20 CGCSL => 9 WXQX
2 BSTCB, 3 HRKD => 9 NLSL
1 MJSQ, 1 BPTV => 8 CGXBG
1 RTRN, 1 RSVR => 3 ZSZBN
2 NZHFV, 1 BSTCB, 20 HRKD => 1 JXVZ
2 BZDPT => 5 HGTL
1 ZSZBN, 14 FDPM => 9 RTML
3 BMXF => 8 FPBTN
1 SDVXW, 8 XRLN => 9 NZHFV
18 QNWRZ, 7 RLFSK => 1 WZLFV"""

calculator = IngridientsCalculator(puzzle_input)

fuel_quantity = 1000000000000 // 387001 # answer from part 1
step = 100000
while True:
    calculator.set_start_product("TOTAL_FUEL", 1, "FUEL", fuel_quantity)
    num_ore = calculator.calculate_ore()    
    print("ore: {} fuel: {}, step: {}".format(num_ore, fuel_quantity, step))

    if num_ore > 1000000000000:
        if step == 1: break
        fuel_quantity -= step
        step //= 10
    fuel_quantity += step