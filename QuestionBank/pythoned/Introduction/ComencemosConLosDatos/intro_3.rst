.. activecode:: intro_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Introduction
    :subchapter: ComencemosConLosDatos
    :topics: Introduction/ComencemosConLosDatos
    :from_source: None
    :caption: Repetición de referencias

    miLista = [1,2,3,4]
    A = [miLista]*3
    print(A)
    miLista[2]=45
    print(A)