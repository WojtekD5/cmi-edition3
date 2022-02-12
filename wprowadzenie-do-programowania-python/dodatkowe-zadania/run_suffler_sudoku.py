from suffler_sudoku import *

sudoku_easy = """
604103209
059008031
137962040
795301062
428600053
361000790
572000304
910230000
840017900
"""

sudoku_middle = """
690405000
001000603
000060000
900013750
030000080
068570009
000050000
807000300
000708091
"""

sudoku_expert = """
000006005
086410000
000020040
000000003
570300000
009000000
090002014
001060090
007080060
"""

sudoku_hard = """
008605000
000000700
000300000
000074050
315000000
000000200
700900064
030120000
000000300
"""

sudoku_str = sudoku_expert
sudoku, hints = solve_sudoku(sudoku_str)
print_sudoku(sudoku)
print_hints(hints)
