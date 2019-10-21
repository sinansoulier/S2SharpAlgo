h1 = [(0, 'val_0'), (2, 'val_2'), (5, 'val_5'), (3, 'val_3'), (1, 'val_1'), (6, 'val_6'), (9, 'val_9'), (4, 'val_4'), (7, 'val_7'), (8, 'val_8')]
h2 = [(33, 'val_33'), (45, 'val_45'), (47, 'val_47'), (19, 'val_19'), (31, 'val_31'), (38, 'val_38'), (17, 'val_17'), (15, 'val_15'), (23, 'val_23'), (1, 'val_1'), (24, 'val_24'), (28, 'val_28'), (26, 'val_26'), (8, 'val_8'), (43, 'val_43'), (39, 'val_39'), (7, 'val_7'), (16, 'val_16'), (13, 'val_13'), (44, 'val_44'), (29, 'val_29'), (40, 'val_40'), (42, 'val_42'), (6, 'val_6'), (2, 'val_2'), (10, 'val_10'), (0, 'val_0'), (27, 'val_27'), (36, 'val_36'), (5, 'val_5'), (20, 'val_20'), (25, 'val_25'), (46, 'val_46'), (35, 'val_35'), (32, 'val_32'), (22, 'val_22'), (30, 'val_30'), (11, 'val_11'), (48, 'val_48'), (34, 'val_34'), (4, 'val_4'), (41, 'val_41'), (14, 'val_14'), (12, 'val_12'), (49, 'val_49'), (18, 'val_18'), (3, 'val_3'), (9, 'val_9'), (21, 'val_21'), (37, 'val_37')]
h3 = [(34, 'val_34'), (81, 'val_81'), (59, 'val_59'), (56, 'val_56'), (79, 'val_79'), (66, 'val_66'), (12, 'val_12'), (63, 'val_63'), (37, 'val_37'), (27, 'val_27'), (24, 'val_24'), (5, 'val_5'), (65, 'val_65'), (62, 'val_62'), (87, 'val_87'), (51, 'val_51'), (85, 'val_85'), (49, 'val_49'), (78, 'val_78'), (25, 'val_25'), (74, 'val_74'), (60, 'val_60'), (67, 'val_67'), (57, 'val_57'), (29, 'val_29'), (4, 'val_4'), (13, 'val_13'), (0, 'val_0'), (88, 'val_88'), (91, 'val_91'), (44, 'val_44'), (10, 'val_10'), (36, 'val_36'), (71, 'val_71'), (23, 'val_23'), (93, 'val_93'), (80, 'val_80'), (70, 'val_70'), (84, 'val_84'), (55, 'val_55'), (18, 'val_18'), (96, 'val_96'), (32, 'val_32'), (89, 'val_89'), (76, 'val_76'), (38, 'val_38'), (86, 'val_86'), (43, 'val_43'), (52, 'val_52'), (3, 'val_3'), (92, 'val_92'), (61, 'val_61'), (77, 'val_77'), (35, 'val_35'), (2, 'val_2'), (54, 'val_54'), (6, 'val_6'), (53, 'val_53'), (97, 'val_97'), (90, 'val_90'), (50, 'val_50'), (46, 'val_46'), (9, 'val_9'), (14, 'val_14'), (58, 'val_58'), (22, 'val_22'), (19, 'val_19'), (17, 'val_17'), (21, 'val_21'), (42, 'val_42'), (47, 'val_47'), (15, 'val_15'), (39, 'val_39'), (26, 'val_26'), (69, 'val_69'), (11, 'val_11'), (75, 'val_75'), (99, 'val_99'), (1, 'val_1'), (94, 'val_94'), (83, 'val_83'), (72, 'val_72'), (16, 'val_16'), (33, 'val_33'), (30, 'val_30'), (73, 'val_73'), (48, 'val_48'), (41, 'val_41'), (20, 'val_20'), (82, 'val_82'), (40, 'val_40'), (28, 'val_28'), (64, 'val_64'), (8, 'val_8'), (68, 'val_68'), (7, 'val_7'), (45, 'val_45'), (95, 'val_95'), (98, 'val_98'), (31, 'val_31')]


H1 = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
H2 = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
H3 = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]

from importlib.machinery import SourceFileLoader
myfile = "/Users/francoissoulier/Desktop/S2SharpAlgo/Algo/Heap_Homework/francois.soulier_heap.py"
francois_soulier_heap = SourceFileLoader('francois_soulier_heap', myfile).load_module()

#print(francois_soulier_heap.is_empty([None]))

#print(H1)
#H4 = H1
#francois_soulier_heap.push(H4, 'N', 5)
#print(H4)
#print (H4 == H2)

#print(francois_soulier_heap.pop(H2))
#H10 = H2
#print(H10)
#print(H10 == H3)

HP = [None]

def push_elements(h):
    for i in h:
        francois_soulier_heap.push(h, i[1], i[0])

def pop_elements(h):
    for i in h:
        print(francois_soulier_heap.pop(h))

push_elements(HP)
print(HP)