fof(eqref,axiom,
     ( ![X]: eq(X,X) )).

fof(eqsym,axiom,
     ( ![X,Y]: ( eq(X,Y) => eq(Y,X) ) )).

fof(eqtrans,axiom,
     ( ![X,Y,Z]: ( ( eq(X,Y) & eq(Y,Z) ) => eq(X,Z) ) )).

fof(eqsub1,axiom,
     ( ![X,Y]: ( eq(X,Y) => ( lives_in_dm(X) <=> ( lives_in_dm(Y) ) ) ) )).

fof(eqsub2,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( killed(X,Z) <=> ( killed(Y,Z) ) ) ) )).

fof(eqsub3,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( killed(Z,X) <=> ( killed(Z,Y) ) ) ) )).

fof(eqsub4,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( hates(X,Z) <=> ( hates(Y,Z) ) ) ) )).

fof(eqsub5,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( hates(Z,X) <=> ( hates(Z,Y) ) ) ) )).

fof(eqsub6,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( richer(X,Z) <=> ( richer(Y,Z) ) ) ) )).

fof(eqsub7,axiom,
     ( ![X,Y,Z]: ( eq(X,Y) => ( richer(Z,X) <=> ( richer(Z,Y) ) ) ) )).

fof(ax1,axiom,
     ( ?[X]: ( lives_in_dm(X) & killed(X,agatha) ) ) ).

fof(ax2,axiom,
     ( ![X]: ( lives_in_dm(X) <=> ( eq(X,agatha) | eq(X,charles) | eq(X,butler)) ) ) ).

fof(ax3,axiom,
     ( ![K,H]: ( killed(K,H) => ( hates(K,H) & ~ richer(K,H) ) ) ) ).

fof(ax4,axiom,
     ( ![H]: ( hates(agatha,H) => ~ hates(charles,H) ) ) ).

fof(ax5,axiom,
     ( ![H]: ( ( ~ eq(butler,H) ) <=> hates(agatha,H) ) ) ).

fof(ax6,axiom,
     ( ![H]: ( ~ richer(H,agatha) => hates(butler,H) ) ) ).

fof(ax7,axiom,
     ( ![H]: ( hates(agatha,H) => hates(butler,H) ) ) ).

fof(ax8,axiom,
     ( ![X]: ?[M]: ~ hates(X,M) )).

fof(ax9,axiom,
     ( ~ eq(agatha,butler) )).

fof(con,conjecture,( killed(agatha,agatha) ) ).
