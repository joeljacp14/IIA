import Ajedrez as ajedrez

estado_inicial = [  # A     B     C     D     E     F     G     H
            '''1''' ["nT", "nC", "nA", "nQ", "nK", "nA", "nC", "nT"],
            '''2''' ["nP", "nP", "nP", "nP", "nP", "nP", "nP", "nP"],
            '''3''' ["__", "__", "__", "__", "__", "__", "__", "__"],
            '''4''' ["__", "__", "__", "__", "__", "__", "__", "__"],
            '''5''' ["__", "__", "__", "__", "__", "__", "__", "__"],
            '''6''' ["__", "__", "__", "__", "__", "__", "__", "__"],
            '''7''' ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            '''8''' ["bT", "bC", "bA", "bQ", "bK", "bA", "bC", "bT"]
                ]

meta = [# jaque mate del loco (se pierde un peon negro, donde esta la reina blanca) GANAN LAS FICHAS BLANCAS
            '''1''' ["nT", "__", "nA", "nQ", "nK", "nA", "__", "nT"],
            '''2''' ["nP", "nP", "nP", "nP", "__", "bQ", "nP", "nP"],
            '''3''' ["__", "__", "nC", "__", "__", "nC", "__", "__"],
            '''4''' ["__", "__", "__", "__", "nP", "__", "__", "__"],
            '''5''' ["__", "__", "bA", "__", "bP", "__", "__", "__"],
            '''6''' ["__", "__", "__", "__", "__", "__", "__", "__"],
            '''7''' ["bP", "bP", "bP", "bP", "__", "bP", "bP", "bP"],
            '''8''' ["bT", "bC", "bA", "__", "bK", "__", "bC", "bT"]
]

raiz = ajedrez.Nodo(estado_inicial)
raiz.imprime_estado()
raiz.expande_peon("b")
