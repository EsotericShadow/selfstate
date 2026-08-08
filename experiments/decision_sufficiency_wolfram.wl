(* ::Package:: *)

(*
  Decision-sufficiency sanity checks for the SelfState formal core.

  Run with:

    wolframscript -file experiments/decision_sufficiency_wolfram.wl

  This script verifies two narrow claims:

  1. Distinct posterior beliefs can induce the same Bayes-optimal action, so
     full posterior recovery is not generally necessary for optimal control.

  2. A shared latent can become description-length efficient as the number of
     contexts that reuse it grows. This is only a compression sanity check; it
     does not establish that the shared latent is agent-bounded.
*)

ClearAll["Global`*"];

(* ------------------------------------------------------------------------- *)
(* Check 1: posterior beliefs collapse into decision-equivalence classes.     *)
(* ------------------------------------------------------------------------- *)

qValue0[p_] := 1 - p;
qValue1[p_] := p;

optimalAction[p_] := Which[
  p < 1/2, 0,
  p > 1/2, 1,
  True, "tie"
];

beliefs = {1/10, 1/4, 2/5, 1/2, 3/5, 3/4, 9/10};

posteriorTable = Table[
  <|
    "posteriorPAgentState1" -> p,
    "qAction0" -> qValue0[p],
    "qAction1" -> qValue1[p],
    "optimalAction" -> optimalAction[p]
  |>,
  {p, beliefs}
];

decisionClasses = GroupBy[posteriorTable, #optimalAction &];

(* Two histories with p=.4 and p=.6 require conflicting optimal actions.     *)
(* If a representation merges them and they are equally likely, the best     *)
(* deterministic action incurs expected regret 0.1.                          *)

historyBeliefs = {2/5, 3/5};
historyWeights = {1/2, 1/2};
actions = {0, 1};

q[p_, action_] := If[action == 0, qValue0[p], qValue1[p]];
value[p_] := Max[qValue0[p], qValue1[p]];

mergedRepresentationRegret = Min@Table[
  Total@Table[
    historyWeights[[i]]*(value[historyBeliefs[[i]]] - q[historyBeliefs[[i]], action]),
    {i, Length[historyBeliefs]}
  ],
  {action, actions}
];

(* ------------------------------------------------------------------------- *)
(* Check 2: toy minimum-description-length reuse inequality.                  *)
(* ------------------------------------------------------------------------- *)

(*
  A latent takes m bits.

  Local encoding in k contexts:  L_local  = k m
  Shared encoding:                L_shared = m + k c

  where c is the per-context interface cost.
*)

localLength[m_, k_] := k*m;
sharedLength[m_, c_, k_] := m + k*c;

reuseInequality = Reduce[
  sharedLength[m, c, k] < localLength[m, k] &&
  m > 0 && 0 <= c < m && k >= 1,
  k,
  Reals
] // FullSimplify;

closedFormThreshold = k > m/(m - c);

reuseExamples = Flatten[
  Table[
    <|
      "latentBits" -> m0,
      "interfaceBits" -> c0,
      "integerContextsForSharing" -> Reduce[
        sharedLength[m0, c0, k] < localLength[m0, k] && k >= 1,
        k,
        Integers
      ]
    |>,
    {m0, {2, 4, 8}},
    {c0, Select[{0, 1, 2}, # < m0 &]}
  ],
  1
];

(* ------------------------------------------------------------------------- *)
(* Verification tests.                                                       *)
(* ------------------------------------------------------------------------- *)

tests = TestReport[{
  VerificationTest[
    DeleteDuplicates[optimalAction /@ {1/10, 1/4, 2/5}],
    {0},
    TestID -> "distinct-posteriors-same-optimal-action-0"
  ],
  VerificationTest[
    DeleteDuplicates[optimalAction /@ {3/5, 3/4, 9/10}],
    {1},
    TestID -> "distinct-posteriors-same-optimal-action-1"
  ],
  VerificationTest[
    mergedRepresentationRegret,
    1/10,
    TestID -> "merged-conflicting-histories-positive-regret"
  ],
  VerificationTest[
    FullSimplify[
      reuseInequality \[Equivalent] closedFormThreshold,
      Assumptions -> {m > 0, 0 <= c < m, k >= 1}
    ],
    True,
    TestID -> "reuse-threshold-equivalence"
  ],
  VerificationTest[
    sharedLength[4, 1, 2] < localLength[4, 2],
    True,
    TestID -> "shared-latent-cheaper-example"
  ]
}];

result = <|
  "posteriorCounterexample" -> <|
    "table" -> posteriorTable,
    "decisionClasses" -> decisionClasses,
    "conclusion" ->
      "Full posterior recovery is sufficient in a POMDP belief-state formulation but is not generally necessary for policy sufficiency."
  |>,
  "conflictingHistoryRegret" -> <|
    "beliefs" -> historyBeliefs,
    "weights" -> historyWeights,
    "minimumDeterministicRegretAfterMerge" -> mergedRepresentationRegret,
    "conclusion" ->
      "A representation that merges histories with disjoint optimal-action sets must incur positive regret on at least one history."
  |>,
  "reusePressure" -> <|
    "symbolicCondition" -> ToString[reuseInequality, InputForm],
    "closedFormThreshold" -> ToString[closedFormThreshold, InputForm],
    "examples" -> reuseExamples,
    "limitation" ->
      "The same compression advantage applies to persistent external world state. Reuse alone does not identify a self-equivalent boundary."
  |>,
  "testsSucceeded" -> tests["TestsSucceeded"],
  "testsFailed" -> tests["TestsFailed"]
|>;

Print[ExportString[result, "RawJSON"]];

If[tests["TestsFailed"] > 0, Exit[1], Exit[0]];
