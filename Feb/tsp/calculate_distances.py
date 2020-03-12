import math

def evaluate(distances, solution):

    r = 0
    n = set()
    print("Solution size: " + str(len(solution)))


    for i in range(len(solution) - 1):
        r += distances[solution[i]-1][solution[i+1]-1]
        if solution[i] in n:
            print("Repeated: " + str(i))
        n.add(solution[i])
    r += distances[solution[-1]-1][solution[0]-1]
    n.add(solution[-1])

    missedItems = [(i + 1) for i in range(318)]
    for i in missedItems:
        if i not in solution:
            print("you miss " + str(i))

    print(len(n))
    return r

input_file = "lin318"
locations = []
with open(input_file, "r") as f:
    for line in f.readlines():
        values = line[:-1:].strip().split()
        locations.append((int(values[1]), int(values[2])))
# print(locations)

n = len(locations)
distances = [[0 for i in range(len(locations))] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        distances[i][j] = int(math.hypot(locations[i][0] - locations[j][0], locations[i][1] - locations[j][1]))
# r = ""
# sol = [int(i) for i in r.split()]
sol=[0,  239,  1,  248,  306,  266,  6,  231,  5,  247,  301,  240,  294,  238,  299,  230,  286,  246,  315,  249,  308,  241,  302,  234,  295,  225,  298,  255,  2,  250,  311,  245,  3,  242,  312,  223,  297,  224,  291,  7,  303,  8,  310,  254,  106,  122,  316,  243,  285,  232,  284,  229,  279,  228,  296,  237,  292,  233,  276,  252,  4,  121,  111,  244,  110,  251,  105,  253,  101,  130,  100,  131,  309,  273,  307,  265,  211,  226,  212,  10,  300,  236,  204,  16,  205,  235,  293,  15,  290,  264,  209,  39,  198,  40,  203,  14,  190,  26,  177,  274,  115,  63,  166,  64,  164,  117,  163,  66,  162,  65,  160,  70,  158,  275,  153,  78,  146,  83,  145,  82,  155,  86,  142,  98,  133,  87,  118,  93,  119,  95,  262,  288,  134,  92,  125,  94,  126,  102,  151,  107,  152,  108,  120,  91,  267,  88,  123,  80,  135,  287,  129,  99,  124,  109,  143,  81,  127,  77,  136,  104,  141,  76,  128,  89,  144,  103,  132,  85,  140,  84,  220,  90,  137,  280,  138,  97,  139,  73,  150,  283,  154,  96,  147,  79,  148,  282,  156,  75,  149,  74,  270,  71,  271,  72,  221,  114,  159,  68,  157,  69,  161,  67,  165,  62,  272,  54,  277,  48,  175,  53,  173,  58,  116,  59,  168,  61,  167,  60,  169,  55,  172,  56,  170,  57,  171,  52,  174,  51,  176,  50,  222,  47,  278,  49,  179,  44,  180,  113,  181,  43,  184,  46,  185,  45,  188,  260,  189,  268,  196,  27,  201,  42,  194,  22,  195,  261,  199,  23,  178,  35,  200,  34,  193,  28,  191,  37,  208,  41,  197,  36,  202,  25,  186,  13,  187,  33,  192,  32,  281,  29,  213,  18,  214,  256,  183,  21,  206,  31,  219,  112,  218,  17,  210,  38,  317,  257,  207,  30,  182,  24,  215,  12,  216,  20,  9,  19,  289,  11,  304,  227,  305,  259,  217,  263,  313,  258,  314,  269]
sol = [i + 1 for i in sol]
print(evaluate(distances, sol))

print(distances)
output_file = "lin318.distances"
# with open(output_file, "w") as f:
#     # f.write("[")
#     for city_dis in distances:
#         # f.write("[")
#         f.write(','.join(map(str, city_dis)))
#         f.write("\n")
#     # f.write("]")

result = []

