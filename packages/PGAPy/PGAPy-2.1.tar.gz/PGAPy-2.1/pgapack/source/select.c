/*
COPYRIGHT

The following is a notice of limited availability of the code, and disclaimer
which must be included in the prologue of the code and in all source listings
of the code.

(C) COPYRIGHT 2008 University of Chicago

Permission is hereby granted to use, reproduce, prepare derivative works, and
to redistribute to others. This software was authored by:

D. Levine
Mathematics and Computer Science Division
Argonne National Laboratory Group

with programming assistance of participants in Argonne National
Laboratory's SERS program.

GOVERNMENT LICENSE

Portions of this material resulted from work developed under a
U.S. Government Contract and are subject to the following license: the
Government is granted for itself and others acting on its behalf a paid-up,
nonexclusive, irrevocable worldwide license in this computer software to
reproduce, prepare derivative works, and perform publicly and display
publicly.

DISCLAIMER

This computer code material was prepared, in part, as an account of work
sponsored by an agency of the United States Government. Neither the United
States, nor the University of Chicago, nor any of their employees, makes any
warranty express or implied, or assumes any legal liability or responsibility
for the accuracy, completeness, or usefulness of any information, apparatus,
product, or process disclosed, or represents that its use would not infringe
privately owned rights.
*/

/*****************************************************************************
*     FILE: select.c: This file contains the routines that have to do with
*                     selection
*
*     Authors: David M. Levine, Philip L. Hallstrom, David M. Noelle,
*              Brian P. Walenz, Ralf Schlatterbeck
*****************************************************************************/

#include "pgapack.h"

/*U****************************************************************************
  INDGetAuxTotal - Compute total value over all aux evaluations

  Category: Operators

  Inputs:
    ind   - Pointer to Individual

  Outputs:
    Computed or cached total value over all aux evaluations
    This is the sum of all *positive* individual aux evaluations.
    The semantics is a total value of all constraint violations.

  Example:
    PGAIndividual *ind = PGAGetIndividual (ctx, p, PGA_OLDPOP);
    double result;
    :
    result = INDGetAuxTotal (ind);

****************************************************************************U*/
double INDGetAuxTotal (PGAIndividual *ind)
{
    PGAContext *ctx = ind->ctx;
    if (!ind->auxtotalok) {
        int i;
        double s = 0;
        int numaux = ctx->ga.NumAuxEval;
        int numcon = ctx->ga.NumConstraint;
        for (i=numaux - numcon; i<numaux; i++) {
            if (ind->auxeval [i] > 0) {
                s += ind->auxeval [i];
            }
        }
        ind->auxtotal   = s;
        ind->auxtotalok = PGA_TRUE;
    }
    return ind->auxtotal;
}

/*U****************************************************************************
  PGAGetAuxTotal - Compute total value over all aux evaluations

  Category: Operators

  Inputs:
    ctx   - context variable
    p     - individual
    pop   - population

  Outputs:
    Computed or cached total value over all aux evaluations
    This is the sum of all *positive* individual aux evaluations.
    The semantics is a total value of all constraint violations.

  Example:
    PGAContext *ctx;
    double result;
    :
    result = PGAGetAuxTotal(ctx, p, PGA_OLDPOP);

****************************************************************************U*/
double PGAGetAuxTotal (PGAContext *ctx, int p, int pop)
{
    PGAIndividual *ind = PGAGetIndividual(ctx, p, pop);
    return INDGetAuxTotal (ind);
}

/*U****************************************************************************
  PGASelect - performs genetic algorithm selection using either the default
  selection scheme or that specified with PGASetSelectType().  Valid selection
  methods are proportional, stochastic universal, tournament, probabilistic
  tournament selection, truncation selection, or linear selection,
  PGA_SELECT_PROPORTIONAL, PGA_SELECT_SUS, PGA_SELECT_TOURNAMENT,
  PGA_SELECT_PTOURNAMENT, PGA_SELECT_TRUNCATION, PGA_SELECT_LINEAR
  respectively. This function updates an internal array with the
  indices of members of popix selected for recombination.  These indices
  may be accessed with PGASelectNextIndex()

  Category: Operators

  Inputs:
    ctx   - context variable
    popix - symbolic constant of population to select from

  Outputs:
    An array used by PGASelectNextIndex() is created which contains the
    population indices of the selected individuals.

  Example:
    PGAContext *ctx,
    :
    PGASelect(ctx, PGA_OLDPOP);

****************************************************************************U*/
void PGASelect (PGAContext *ctx, int popix)
{
    int i;                   /* not to intefere with dummy argument        */
    int j;                   /* random number                              */
    int temp;                /* for shuffling selected indices US          */
    PGAIndividual *pop;      /* pointer to appropriate population          */

    PGADebugEntered("PGASelect");

    pop = PGAGetIndividual(ctx, 0, popix);

    switch (ctx->ga.SelectType) {

    case PGA_SELECT_PROPORTIONAL:  /* proportional selection             */
        for (i=0; i<ctx->ga.PopSize; i++)
            ctx->ga.selected[i] = PGASelectProportional (ctx, pop);
        break;
    case PGA_SELECT_SUS:           /* stochastic universal selection     */
        PGASelectSUS( ctx, pop );
        break;
    case PGA_SELECT_TOURNAMENT:    /* tournament selection               */
        for (i=0; i<ctx->ga.PopSize; i++)
            ctx->ga.selected[i] = PGASelectTournament (ctx, popix);
        break;
    case PGA_SELECT_PTOURNAMENT:   /* probabilistic tournament selection */
        for (i=0; i<ctx->ga.PopSize; i++)
            ctx->ga.selected[i] = PGASelectPTournament (ctx, popix);
        break;
    case PGA_SELECT_TRUNCATION:   /* truncation selection */
        for (i=0; i<ctx->ga.PopSize; i++)
            ctx->ga.selected[i] = PGASelectTruncation (ctx, popix);
        break;
    case PGA_SELECT_LINEAR:      /* linear selection */
        for (i=0; i<ctx->ga.PopSize; i++)
            ctx->ga.selected[i] = PGASelectLinear (ctx, pop);
        break;
    default:
        PGAError( ctx,
                 "PGASelect: Invalid value of SelectType:",
                  PGA_FATAL,
                  PGA_INT,
                  (void *) &(ctx->ga.SelectType) );
        break;
    }

    /* randomize selected string locations
     * Note that for all selection schemes above *except* SUS the items
     * are already randomized. So we randomize only if the selection
     * scheme is SUS *or* we have the backward-compatibility flag
     * ctx->ga.RandomizeSelect set. Note that the point of linear
     * selection is that the sequence is *not* randomized. So in this
     * case we never randomize the sequence.
     */
    if  (  ctx->ga.SelectType == PGA_SELECT_SUS
        || (  ctx->ga.RandomizeSelect
           && ctx->ga.SelectType != PGA_SELECT_LINEAR
           )
        )
    {
        for (i=0; i<ctx->ga.PopSize; i++) {
            j          = PGARandomInterval(ctx, 0,ctx->ga.PopSize-1);
            temp       = ctx->ga.selected[j];
            ctx->ga.selected[j] = ctx->ga.selected[i];
            ctx->ga.selected[i] = temp;
        }
    }

    PGADebugExited("PGASelect");
}

/*U****************************************************************************
  PGASelectNextIndex - returns the index of next individual in
  internal array that contains the indices determined by PGASelect

  Category: Operators

  Inputs:
    ctx   - context variable
    popidx - the population index, typically PGA_OLDPOP

  Outputs:
    A population index for the next selected creature.

  Example:
    PGAContext *ctx;
    int l;
    :
    l = PGASelectNextIndex(ctx, PGA_OLDPOP);

****************************************************************************U*/
int PGASelectNextIndex (PGAContext *ctx, int popix)
{
    PGADebugEntered("PGASelectNextIndex");

    /* We allow the select to consume more than ga.PopSize items
     * If more are consumed we need to prepare the next batch.
     */
    if (ctx->ga.SelectIndex >= ctx->ga.PopSize) {
        PGASelect (ctx, popix);
        ctx->ga.SelectIndex = 0;
    }

    PGADebugExited("PGASelectNextIndex");
    return(ctx->ga.selected[ctx->ga.SelectIndex++]);
}

/*U****************************************************************************
   PGASetSelectType - specify the type of selection to use. Valid choices
   are PGA_SELECT_PROPORTIONAL, PGA_SELECT_SUS, PGA_SELECT_TOURNAMENT, and
   PGA_SELECT_PTOURNAMENT for proportional, stochastic universal selection,
   tournament, and probabilistic tournament selection, respectively.  The
   default is PGA_SELECT_TOURNAMENT.

   Category: Operators

   Inputs:
      ctx         - context variable
      select_type - symbolic constant to specify selection type

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetSelectType(ctx, PGA_SELECT_SUS);

****************************************************************************U*/
void PGASetSelectType( PGAContext *ctx, int select_type)
{

    PGADebugEntered("PGASetSelectType");

    switch (select_type) {
        case PGA_SELECT_PROPORTIONAL:
        case PGA_SELECT_SUS:
        case PGA_SELECT_TOURNAMENT:
        case PGA_SELECT_PTOURNAMENT:
        case PGA_SELECT_TRUNCATION:
        case PGA_SELECT_LINEAR:
            ctx->ga.SelectType = select_type;
            break;
        default:
            PGAError ( ctx, "PGASetSelectType: Invalid value of select_type:",
                      PGA_FATAL, PGA_INT, (void *) &select_type);
        break;
    }

    PGADebugExited("PGASetSelectType");
}

/*U***************************************************************************
   PGAGetSelectType - Returns the type of selection selected

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      Returns the integer corresponding to the symbolic constant
      used to specify the type of selection specified

   Example:
      PGAContext *ctx;
      int selecttype;
      :
      selecttype = PGAGetSelectType(ctx);
      switch (selecttype) {
      case PGA_SELECT_PROPORTIONAL:
          printf ("Selection Type = PGA_SELECT_PROPORTIONAL\n");
          break;
      case PGA_SELECT_SUS:
          printf ("Selection Type = PGA_SELECT_SUS\n");
          break;
      case PGA_SELECT_TOURNAMENT:
          printf ("Selection Type = PGA_SELECT_TOURNAMENT\n");
          break;
      case PGA_SELECT_PTOURNAMENT:
          printf ("Selection Type = PGA_SELECT_PTOURNAMENT\n");
          break;
      case PGA_SELECT_TRUNCATION:
          printf ("Selection Type = PGA_SELECT_TRUNCATION\n");
          break;
      }

***************************************************************************U*/
int PGAGetSelectType (PGAContext *ctx)
{
    PGADebugEntered("PGAGetSelectType");
    PGAFailIfNotSetUp("PGAGetSelectType");

    PGADebugExited("PGAGetSelectType");

    return(ctx->ga.SelectType);
}


/*U****************************************************************************
   PGASetPTournamentProb - Specifies the probability that the string that wins
   a binary tournament will be selected.  This function will have no effect
   unless PGA_SELECT_PTOURNAMENT was specified as the type of selection to
   use with PGASetSelectType.  The default value is 0.6.

   Category: Operators

   Inputs:
      ctx - context variable
      p   - the probability of selecting the better string

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetPTournamentProb(ctx,0.8);

****************************************************************************U*/
void PGASetPTournamentProb(PGAContext *ctx, double ptournament_prob)
{
    PGADebugEntered("PGASetPTournamentProb");

    ctx->ga.PTournamentProb = ptournament_prob;

    PGADebugExited("PGASetPTournamentProb");
}

/*U***************************************************************************
   PGAGetPTournamentProb - returns the probability of selecting the best
   string in a probabilistic binary tournament

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      The probabilistic binary tournament selection probability

   Example:
      PGAContext *ctx;
      double pt;
      :
      pt = PGAGetPTournamentProb(ctx);

***************************************************************************U*/
double PGAGetPTournamentProb(PGAContext *ctx)
{
    PGADebugEntered("PGAGetPTournamentProb");
    PGAFailIfNotSetUp("PGAGetPTournamentProb");

    PGADebugExited("PGAGetPTournamentProb");

     return ctx->ga.PTournamentProb;
}

/*U****************************************************************************
   PGASetTournamentSize - Specifies the number of participants in a
   non-probabilistic Tournament
   This function will have no effect unless PGA_SELECT_TOURNAMENT was
   specified as the type of selection to use with PGASetSelectType.  The
   default value is 2.

   Category: Operators

   Inputs:
      ctx - context variable
      sz  - the size of the tournament

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetTournamentSize(ctx,3);

****************************************************************************U*/
void PGASetTournamentSize (PGAContext *ctx, double tournament_size)
{
    PGADebugEntered ("PGASetTournamentSize");

    ctx->ga.TournamentSize = tournament_size;

    PGADebugExited ("PGASetTournamentSize");
}

/*U***************************************************************************
   PGAGetTournamentSize - returns the number of participants in a
   tournament

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      The number of participants in a non probabilistic tournament

   Example:
      PGAContext *ctx;
      double sz;
      :
      sz = PGAGetTournamentSize (ctx);

***************************************************************************U*/
double PGAGetTournamentSize (PGAContext *ctx)
{
    PGADebugEntered ("PGAGetTournamentSize");
    PGAFailIfNotSetUp("PGAGetTournamentSize");

    PGADebugExited ("PGAGetTournamentSize");

    return ctx->ga.TournamentSize;
}
/*U****************************************************************************
   PGASetTournamentWithReplacement - Specifies if tournament is with or
   without replacement. This function will have no effect unless
   PGA_SELECT_TOURNAMENT was specified as the type of selection to use
   with PGASetSelectType. The default value is PGA_TRUE.

   Category: Operators

   Inputs:
      ctx - context variable
      v   - The value, PGA_TRUE or PGA_FALSE

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetTournamentWithReplacement(ctx,PGA_FALSE);

****************************************************************************U*/
void PGASetTournamentWithReplacement(PGAContext *ctx, int v)
{
    ctx->ga.TournamentWithRepl = v;
}

/*U***************************************************************************
   PGAGetTournamentWithReplacement - returns the setting for tournament
   sampling: with replacement returns PGA_TRUE, without replacement
   returns PGA_FALSE.

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      The setting of tournament with/without replacement, PGA_TRUE if
      with replacement

   Example:
      PGAContext *ctx;
      int v;
      :
      v = PGAGetTournamentWithReplacement(ctx);

***************************************************************************U*/
int PGAGetTournamentWithReplacement(PGAContext *ctx)
{
    PGAFailIfNotSetUp("PGAGetTournamentWithReplacement");
    return ctx->ga.TournamentWithRepl;
}
/*U****************************************************************************
   PGASetTruncationProportion - Specifies the proportion of selected
   individuals for truncation selection. This function will have no
   effect unless PGA_SELECT_TRUNCATION was specified as the type of
   selection to use with PGASetSelectType. The default value is 0.5.

   Category: Operators

   Inputs:
      ctx - context variable
      proportion - The value, 0 < proportion <= 1

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetTruncationProportion(ctx, 0.7);

****************************************************************************U*/
void PGASetTruncationProportion(PGAContext *ctx, double proportion)
{
    PGAFailIfSetUp("PGASetTruncationProportion");
    ctx->ga.TruncProportion = proportion;
}

/*U***************************************************************************
   PGAGetTruncationProportion - returns the setting for truncation
   proportion.

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      The truncation proportion

   Example:
      PGAContext *ctx;
      double v;
      :
      v = PGAGetTruncationProportion(ctx);

***************************************************************************U*/
double PGAGetTruncationProportion(PGAContext *ctx)
{
    PGAFailIfNotSetUp("PGAGetTruncationProportion");
    return ctx->ga.TruncProportion;
}
/*U****************************************************************************
   PGASetRandomizeSelect - Specifies if during PGASelect the chosen
   individuals should be randomized again. All selection schemes except
   PGA_SELECT_SUS already return the individuals in randomized order,
   previously this was randomized again. With this method you can
   re-enable the randomization for selection schemes other than
   PGA_SELECT_SUS (for which a randomization step is always performed).

   Category: Operators

   Inputs:
      ctx - context variable
      v - The value, PGA_FALSE or PGA_TRUE

   Outputs:
      None

   Example:
      PGAContext *ctx;
      :
      PGASetRandomizeSelect(ctx, PGA_TRUE);

****************************************************************************U*/
void PGASetRandomizeSelect(PGAContext *ctx, int v)
{
    ctx->ga.RandomizeSelect = v;
}

/*U***************************************************************************
   PGAGetRandomizeSelect - returns the setting for additional select
   randomization.

   Category: Operators

   Inputs:
      ctx - context variable

   Outputs:
      The setting of select randomization

   Example:
      PGAContext *ctx;
      int v;
      :
      v = PGAGetRandomizeSelect(ctx);

***************************************************************************U*/
int PGAGetRandomizeSelect(PGAContext *ctx)
{
    PGAFailIfNotSetUp("PGAGetTruncationProportion");
    return ctx->ga.RandomizeSelect;
}



/*I****************************************************************************
  PGASelectProportional - selects a parent for the next generation using a
  linear search through a (fitness) weighted ``roulette wheel''.  The
  probability of selection is given by p_i = f_i/sum(i)f_i
  Ref: D. Goldberg, Genetic Algorithms, pg.

  Inputs:
    ctx   - context variable
    popix - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectProportional(ctx, PGA_OLDPOP);

****************************************************************************I*/
int PGASelectProportional(PGAContext *ctx, PGAIndividual *pop)
{
    double sum, sumfitness, r;
    int i;

    PGADebugEntered("PGASelectProportional");

    sumfitness = 0.0;
    for (i=0; i<ctx->ga.PopSize; i++)
        sumfitness += (pop+i)->fitness;

    i = 0;
    sum = (pop+i)->fitness;

    r = sumfitness * PGARandom01(ctx, 0);
    while(r > sum || i==ctx->ga.PopSize) {
        i++;
        sum += (pop+i)->fitness;
    }

    PGADebugExited("PGASelectProportional");

    return(i);
}

/*I****************************************************************************
  PGASelectSUS - A select routine using stochastic universal sampling
  Ref:    J. Baker, Reducing Bias and Inefficiency in the Selection Algorithm.
  Second GA conference, pp 14-21 (page 16)

  Inputs:
    ctx   - context variable
    popix - symbolic constant of population to select from

  Outputs:
    the array ga.selected[] created via side effect.  I.e., this routine
    creates the entire selected population with one call

  Example:
    PGAContext *ctx,
    :
    PGASelectSUS(ctx, PGA_OLDPOP);

****************************************************************************I*/
void PGASelectSUS( PGAContext *ctx, PGAIndividual *pop )
{
    int i;
    int k;                          /* index to fill samples array    */
    double davg;                    /* population average fitness     */
    double sum;                     /* running sum of expected values */
    double r;                       /* random number                  */

    PGADebugEntered("PGASelectSUS");

    /* fill the expected value array */
    davg = 0.0;
    for(i=0;i<ctx->ga.PopSize;i++)
        davg += (pop+i)->fitness;
    davg /=  (double) ctx->ga.PopSize;
    for(i=0;i<ctx->ga.PopSize;i++)
        ctx->scratch.dblscratch[i] = (pop+i)->fitness / davg;

    /* select ctx->ga.PopSize as follows */
    sum = 0;
    k   = 0;
    r   = PGARandom01(ctx, 0);
    for(i=0;i<ctx->ga.PopSize;i++)
        for( sum+=ctx->scratch.dblscratch[i]; sum>r; r++ )
            ctx->ga.selected[k++] = i;

    PGADebugExited("PGASelectSUS");
}


/*I****************************************************************************
  PGASelectTournamentWithReplacement - chooses N strings randomly and
  returns the one with best evaluation, N is the value set with
  PGASetTournamentSize, the default is 2. The selection happens *with*
  replacement. See decription of PGASelectTournamentWithoutReplacement
  for details of sampling without replacement.
  Ref:    Generalization of D. Goldberg, Genetic Algorithms, pg. 121
          For the generalization see, e.g., D. E. Goldberg and K. Deb
          A Comparative Analysis of Selection Schemes Used in Genetic
          Algorithms, in Gregory J. E. Rawlins (Ed.) Foundation of
          Genetic Algorithms (FOGA) 1, pp. 69-93, 1991.

  Inputs:
    ctx - context variable
    pop - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectTournamentWithReplacement(ctx, PGA_OLDPOP);

****************************************************************************I*/
static
int PGASelectTournamentWithReplacement (PGAContext *ctx, int pop)
{
    int i;
    int m = PGARandomInterval (ctx, 0, ctx->ga.PopSize-1);
    int t = (int)ctx->ga.TournamentSize;
    if (ctx->ga.TournamentSize - t) {
        t += PGARandomFlip (ctx, ctx->ga.TournamentSize - t);
    }
    for (i=1; i<t; i++) {
        int mn = PGARandomInterval(ctx, 0, ctx->ga.PopSize-1);
        /* use '<=' for backwards-compat with prev. binary tournament */
        if (PGAEvalCompare (ctx, mn, pop, m, pop) <= 0) {
            m = mn;
        }
    }
    return m;
}

/*I****************************************************************************
  PGASelectTournamentWithoutReplacement - chooses N strings randomly and
  returns the one with best evaluation, N is the value set with
  PGASetTournamentSize, the default is 2. The selection happens *without*
  replacement. This means if we select N individuals with a tournament
  size of 2, each individual is participating in exactly two
  tournaments. This does *not* mean that a single individual cannot be
  returned more than once.
  Ref:    For implementation notes on the algorithm see p.504 in
          David E. Goldberg, Bradley Korb, and Kalyanmoy Deb. Messy
          genetic algorithms: Motivation, analysis, and first results.
          Complex Systems, 3(5):493–530, 1989.

  Inputs:
    ctx - context variable
    pop - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectTournamentWithoutReplacement(ctx, PGA_OLDPOP);

****************************************************************************I*/


/* Helper function to compute permuted list */
static void _shuffle (PGAContext *ctx, int k, int init)
{
    if (init) {
        int i = 0;
        for (i=0; i<k; i++) {
            ctx->scratch.permute [i] = i;
        }
    }
    PGAShuffle (ctx, ctx->scratch.permute, k);
}
#define NEXT_IDX(ctx, k, init)                        \
    ((ctx)->ga.perm_idx >= (k))                       \
    ? ( _shuffle((ctx), (k), (init))                  \
      , (ctx)->ga.perm_idx = 1                        \
      , (ctx)->scratch.permute [0]                    \
      )                                               \
    : ctx->scratch.permute [ctx->ga.perm_idx++]

static
int PGASelectTournamentWithoutReplacement (PGAContext *ctx, int pop)
{
    int m;
    int i;
    int t = (int)ctx->ga.TournamentSize;

    if (ctx->ga.TournamentSize - t) {
        t += PGARandomFlip (ctx, ctx->ga.TournamentSize - t);
    }

    m = NEXT_IDX(ctx, ctx->ga.PopSize, 1);
    assert (0 <= m && m < ctx->ga.PopSize);
    for (i=1; i<t; i++) {
        int mn = NEXT_IDX(ctx, ctx->ga.PopSize, 1);
        assert (0 <= mn && mn < ctx->ga.PopSize);
        if (PGAEvalCompare (ctx, mn, pop, m, pop) <= 0) {
            m = mn;
        }
    }
    return m;
}

/*I****************************************************************************
  PGASelectLinear - chooses all strings that are not already copied to
  the next generation due to elitist strategies. Note that this
  'selection' scheme isn't a selection scheme in the genetic sense, it
  has no selection pressure. Note that the indeces are *not randomized.

  Inputs:
    ctx   - context variable
    popix - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectLinear (ctx, PGA_OLDPOP);

****************************************************************************I*/
int PGASelectLinear (PGAContext *ctx, PGAIndividual *pop)
{
    int numreplace = PGAGetNumReplaceValue (ctx);
    int popsize = PGAGetPopSize (ctx);

    if (ctx->ga.last_iter != ctx->ga.iter || ctx->ga.perm_idx >= popsize) {
        ctx->ga.perm_idx  = popsize - numreplace;
        ctx->ga.last_iter = ctx->ga.iter;
    }
    return ctx->ga.perm_idx++;
}

/*I****************************************************************************
  PGASelectTruncation - chooses the best k strings and returns them in
  random order. The value k is (N * TruncationProportion) rounded to the
  next integer.

  Inputs:
    ctx - context variable
    pop - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectTruncation (ctx, PGA_OLDPOP);

****************************************************************************I*/
int PGASelectTruncation (PGAContext *ctx, int pop)
{
    int m = -1;
    int k = (int)(ctx->ga.PopSize * ctx->ga.TruncProportion + 0.5);

    if (k < 1) {
        k = 1;
    }
    if (k > ctx->ga.PopSize) {
        k = ctx->ga.PopSize;
    }

    if (ctx->ga.last_iter != ctx->ga.iter) {
        int i;
        DECLARE_DYNARRAY (int, bestidx, ctx->ga.PopSize);
        /* Returns sorted list of indeces in bestidx, no need to initialize */
        PGAEvalSort (ctx, pop, bestidx);
        /* Copy the k first indeces */
        for (i=0; i<k; i++) {
            ctx->scratch.permute [i] = bestidx [i];
        }
        ctx->ga.last_iter = ctx->ga.iter;
        ctx->ga.perm_idx  = k;
    }

    m = NEXT_IDX(ctx, k, 0);
    assert (0 <= m && m < ctx->ga.PopSize);
    return m;
}

/*I****************************************************************************
  PGASelectTournament - chooses N strings randomly and
  returns the one with best evaluation, N is the value set with
  PGASetTournamentSize, the default is 2. Depending on the setting of
  PGASetTournamentWithReplacement calls one of two local functions to
  use the right sampling.

  Inputs:
    ctx - context variable
    pop - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectTournament(ctx, PGA_OLDPOP);

****************************************************************************I*/
int PGASelectTournament (PGAContext *ctx, int pop)
{
    PGADebugEntered("PGASelectTournament");
    if (ctx->ga.TournamentWithRepl) {
        return PGASelectTournamentWithReplacement (ctx, pop);
    } else {
        return PGASelectTournamentWithoutReplacement (ctx, pop);
    }
    PGADebugExited("PGASelectTournament");
}

/*I****************************************************************************
  PGASelectPTournament - chooses two strings randomly and returns the one with
  better evaluation with a specified probability
  Ref:    D. Goldberg, Genetic Algorithms, pg. 121

  Inputs:
    ctx - context variable
    pop - symbolic constant of population to select from

  Outputs:
    index of the selected string

  Example:
    PGAContext *ctx,
    int l;
    :
    l = PGASelectPTournament(ctx, PGA_OLDPOP);

****************************************************************************I*/
int PGASelectPTournament (PGAContext *ctx, int pop)
{
    int m1, m2;
    int RetVal;
    double drand;

    PGADebugEntered("PGASelectPTournament");

    m1 = PGARandomInterval(ctx, 0, ctx->ga.PopSize-1);
    m2 = PGARandomInterval(ctx, 0, ctx->ga.PopSize-1);
    drand = PGARandom01 (ctx, 0);

    if (PGAEvalCompare (ctx, m1, pop, m2, pop) < 0) {
        RetVal = drand < ctx->ga.PTournamentProb ? m1 : m2;
    } else {
        RetVal = drand < ctx->ga.PTournamentProb ? m2 : m1;
    }

    PGADebugExited("PGASelectPTournament");
    return(RetVal);
}
