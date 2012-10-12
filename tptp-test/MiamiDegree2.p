fof(degree,axiom,
    ( ( composition & humanities & science & math & social_science & language
      & writing )
    => degree ) ).

fof(composition,axiom,
    ( ( eng105 & eng106 )
    => composition ) ).

fof(composition_courses,axiom,
    ( eng105 & eng106 ) ).

fof(humanities,axiom,
    ( ( art & literature & religion & phi115 )
    => humanities ) ).

fof(art,axiom,
    ( ( artXXX | arhXXX | danXXX | mcyXXX | thaXXX )
    => art ) ).

fof(artXXX,axiom,artXXX ).

fof(literature,axiom,
    ( eng2XX
    => literature ) ).

fof(literature_courses,axiom,
    ( eng2XX ) ).

fof(religion,axiom,
    ( relXXX
    => religion ) ).

fof(religion_courses,axiom,
    ( relXXX ) ).

fof(phi115,axiom,
    ( phi115 ) ).

fof(science,axiom,
    ( ( bilXXX | chmXXX | ecsXXX | geoXXX | mscXXX | phyXXX )
    => science ) ).

fof(phyXXX,axiom,phyXXX ).

fof(math,axiom,
    ( ( mth162 & ( cscXXX | staXXX) )
    => math ) ).

fof(mth162,axiom,mth162 ).
fof(cscXXX,axiom,cscXXX ).

fof(social_science,axiom,
    ( ( apyXXX | ecoXXX | gegXXX | hisXXX | intXXX | polXXX | psyXXX | socXXX )
    => social_science ) ).

fof(ecoXXX,axiom,ecoXXX ).

fof(language,axiom,
    ( ( arb2XX | chi2XX | fre2XX | ger2XX | gre2XX | heb2XX | ita2XX | jap2XX |
        lat2XX | por2XX | spa2XX )
    => language ) ).

fof(arbXXX,axiom,arb2XX ).

fof(wwwXXX_writing,axiom,
    wwwXXX => writing ).

fof(wwwXXX,axiom,wwwXXX).

fof(hisXXX_writing,axiom,
    hisXXX => writing ).
fof(eng2XX_writing,axiom,
    eng2XX => writing ).

fof(phi115_writing,axiom,
    phi115 => writing ).

fof(get_degree,conjecture,
    degree ).
