---
layout: post
title: "After AI Finds a New Method: Axioms and Tests for Understanding"
date: 2026-10-08 11:30:00 +0800
last_modified_at: 2026-10-08 19:09:59 +0800
lang: en
permalink: /en/posts/understanding-without-possessing-the-world/
alternate_url: /posts/understanding-without-possessing-the-world/
categories: [AI, Philosophy]
tags: [Artificial Intelligence, Epistemology, Axiomatization, Understanding, Mathematics, Revisability]
description: "Recent Claude algorithms and OpenAI mathematics manuscripts make discovery, verification, explanation, and revision concrete. Three axioms expose the information, computation, and evidence each claim of understanding requires."
toc: true
comments: true
math: true
---

<span id="s1"></span>

## What did Claude actually change?
{: #proof }

On October 5, 2026, Josh Alman and Virginia Vassilevska Williams published an algorithms preprint giving a deterministic $$O(n^{1.9992})$$ algorithm for 3SUM on polynomial-size integers and an $$O(n^{2.9995})$$ bound for all-pairs shortest paths, or APSP, on directed graphs with polynomially bounded integer weights. The results refute the corresponding 3SUM and APSP hypotheses.[^algorithm]

3SUM asks whether an input contains three numbers whose sum is zero. For example, −4, 1, and 3 form a solution. With a few numbers, the task is easy; the question is how the work grows with the input. APSP asks for the shortest distance between every pair of vertices in a graph. Cities and roads provide an intuitive example, but the paper's asymptotic bounds cannot be read as measurements of navigation software.

The change from an exponent of 2 to 1.9992 looks small. Its significance is that the reduction is a fixed positive amount: comparing these powers, the asymptotic saving continues to grow with the input. This differs from making the same program twice as fast, and is stronger than saving only logarithmic factors. Constants, input regimes, and implementation costs can still make a new method slower at ordinary scales. **The breakthrough concerns conjectured asymptotic barriers. It does not overturn a proved lower bound or establish an immediate practical speedup.**

The paper's methodology credits Claude with discovering the key algorithm during a research session that received no further human input after the initial task. Human authors subsequently organized, strengthened, and extended the work, taking responsibility for the paper. Lean formalization of the principal results followed completion of the manuscript.[^method] Autonomous discovery of the central method and a wholly human-free research project are different claims.

Understanding can now be investigated through specific work: finding an algorithm, checking it, explaining why it works, and determining whether it applies to a modified problem. Success at one task does not automatically establish success at the others.

**A claim of understanding should identify its object, the questions it covers, the changes it can handle, its supporting evidence, and its resource requirements.** The same demand applies to a researcher, an AI system, or a research process combining both.

<span id="s2"></span>

## 722 manuscripts, followed by three withdrawals
{: #ledger }

The next day, OpenAI released mathematical work from an internal model, together with some Lean proofs and information about the research process. Lean is a proof assistant: formalization expresses precise statements and derivations in a form a program can check.[^release] The initial collection listed 722 manuscripts across 372 result families. A manuscript count is not a count of fully confirmed new theorems.[^catalogue]

The October 7 revision log records a concrete failure. A sign error in *Algebraicity of Weil classes on split abelian eightfolds* invalidated an argument and a construction used in two dependent manuscripts. All three were withdrawn. The current collection lists 719 manuscripts, with 300 top-line results—the manuscripts' principal claims—formalized, approximately 42%. These are the versioned figures consulted on October 8.[^history]

The initial count describes the scale of production. The corrections describe how that production becomes material for further research. Both matter.

When a proof step fails, arguments relying on it lose their existing justification. Their conclusions may still be true, and another proof may later establish them. Immediately declaring them false would go beyond the evidence, just as continuing to treat the failed proofs as valid would.

This episode supplies concrete tests of understanding. Can a system locate the defect? Identify other arguments that depend on it? Repair the proof without quietly weakening the theorem? A list of conclusions and an aggregate score cannot answer these questions.

![Versioned OpenAI manuscript counts: 722 initially, 719 after three withdrawals, with 300 top-line results formalized.](/assets/img/articles/aei-v4-release-status.webp){: width="1200" height="1060" }
_Figure 1. Public catalogue and October 7, 2026 revision log. Formalization status does not establish novelty, explanatory quality, or the suitability of every external assumption. Lack of formalization does not establish an error._

<span id="s3"></span>

## Three axioms for a tractable philosophical question
{: #axioms }

“Real understanding must resemble human thinking” is difficult to test. “Any correct answer counts as understanding” is too permissive: memorization, a lucky guess, and a reliable explanation can receive the same score.

Axiomatization can begin by specifying an assessment: the permitted situations, the questions, the available materials, and the resource budget. Three conditions then remain fixed.

**First, keep the criterion stable within an assessment.** Algorithmic correctness calls for checking inputs, outputs, and proofs. Explanatory ability calls for identifying important steps and why they matter. Adding a requirement only after discovering that the author is AI changes the test. Substituting a speed result for correctness changes it too. New criteria may be proposed, but should be identified as new assessments.

**Second, answers must depend on materials and computations actually available to the system.** Model parameters, context, tools, documents, and information from collaborators all count. An unread external file cannot be treated as already known. More deliberation cannot be assumed to recover evidence that has been discarded.

**Third, account for the cost of obtaining and using those materials.** Search, deduction, formalization, proof checking, and expert review consume different resources. A comparison is distorted if one system receives a proof for free while another must discover it. Time, computation, and human labor also require an explicit conversion rule before they can be combined into one quantity.

These axioms do not define consciousness or establish general intelligence. They first constrain something smaller: how to assess a claim about understanding fairly.

Let $$x$$ denote the actual situation, $$r(x)$$ the record available to the system, and $$q(x)$$ the correct answer to a question. The notation makes it harder to introduce information or change the task unnoticed.

<span id="s4"></span><span id="s6"></span><span id="s7"></span><span id="s9"></span>

## First consequence: retaining an answer can erase the ability to follow it up
{: #distinctions }

Several different questions can be asked about the mathematics collection.

| Question | Materials to check |
| :-- | :-- |
| Is this version listed as formalized? | The relevant status record and version mapping |
| Which assumptions does the proof use? | The precise statement, dependencies, and proof |
| Which arguments require review after a lemma fails? | Proof dependency records |
| Does the conclusion survive a changed condition? | The original proof, a replacement argument, or a counterexample |

These are different requirements. Keeping the word “passed” may answer a status query without supporting any of the other questions. The difference concerns which situations the retained record can distinguish.

**Proposition 1. A record is sufficient for a set of questions exactly when all situations producing the same record give the same answers to those questions.**

For every relevant question $$q$$, the condition is:

$$
r(x)=r(y)\ \Longrightarrow\ q(x)=q(y).
$$

Necessity is immediate: identical available records cannot guarantee different correct answers. Conversely, if every situation associated with a record gives the same answer, that answer can be assigned to the record. This establishes informational determination, not an efficient algorithm for computing the answer.

A further result follows: **adding questions can make a previously sufficient summary insufficient.** If the original questions are $$Q$$ and $$Q\subseteq Q'$$, the distinctions required for $$Q'$$ can only increase or remain unchanged. An old summary remains sufficient only if it already determines the answers to the added questions.

Research records therefore cannot be evaluated only against today's examination. Retaining an algorithm's exponent may answer “What is the bound?” A later question about which step imposes an input restriction requires the derivation.

Understanding has a scope. A representation can support one collection of questions while failing another. The boundary can be exhibited, rather than left to an unexplained judgment that a system “really gets it.”

<span id="s18"></span>

## Second consequence: repeated self-checking cannot guarantee recovery of missing evidence
{: #diagnosis }

Two obstacles need to be separated.

The first is **available information that has not yet been processed**. A full proof may already be present, while checking a step requires more deduction or formalization. Additional computation can produce a new answer without new external observations.

The second is **a distinction absent from the available record**. Suppose two research records retain only the same “checked” label, but one refers to the wrong version. Without access to the version and execution records, repeating the label cannot reveal which case applies.

**Proposition 2. A perfect error detector using only the current record exists only if that record uniquely determines whether the answer is erroneous.**

This applies Proposition 1 to the question “Is this answer wrong?” It does not prohibit risk estimates or referral of every ambiguous case for review. It rules out guaranteed case-by-case diagnosis where the distinguishing evidence is missing.

Whether “think again” helps depends on the obstacle. A missed inference may yield to additional computation. A missing version requires a version check. A translation into a weaker formal statement requires comparison of the statements. One instruction cannot substitute for all these tasks.

A Lean check provides evidence that a formal statement follows within a specified formal system and its dependencies. Whether the prose describes that statement accurately, and whether its assumptions fit the intended problem, remain separately examinable questions.

Explicit probability and cost assumptions also make verification requirements calculable. Suppose each case has a 10% error probability invisible in its current summary. Selection for checking is independent of actual error; unchecked cases retain their original answers; and a perfect check eliminates the error in every checked case. If the checked fraction is $$\rho$$, the expected remaining error rate is:

$$
0.1(1-\rho).
$$

Within this process, reducing the expected error rate to 1% requires checking at least 90% of cases. **The percentages are assumptions of this example, not measured error rates for OpenAI manuscripts or Claude.** Useful risk signals or fallible checks require a different model.

The calculation exposes a practical cost: producing many candidate answers does not by itself supply the resources needed to raise all of them to a specified reliability standard.

<span id="s8"></span><span id="s10"></span>

## Third consequence: better algorithms change what is feasible
{: #laws }

The Claude result concerns an obstacle different from missing information. For a fully specified 3SUM input, the answer does not depend on an unpublished external record. The obstacle is computational cost. A new algorithm can change what is feasible without adding input information.

**Informational sufficiency and resource sufficiency require separate assessments.** Proposition 1 addresses the former; complexity analysis addresses the latter. Calling something currently unaffordable “unknowable in principle” mistakes room for algorithmic improvement for a final limit of cognition.

Understanding claims therefore need resource conditions. A method may have a theoretical capability without being useful under the available budget. Better methods can make the same data support a wider practical range of questions.

**Proposition 3. If the set of available methods expands while old methods remain available and the criterion and budget stay fixed, the set of solvable questions cannot shrink.** Every previously feasible method remains an option. A cheaper new method may also bring previously unaffordable questions within budget. This does not make every new method faster.

A recent biomolecular-modeling project illustrates another side of this distinction. Anthropic reported roughly fourfold overall speedups when very small numerical differences were permitted, and nearly twofold speedups with identical outputs.[^bio]

The same report describes much larger structure-prediction runs, ranging from 31,000 to over 70,000 tokens on one eight-GPU B300 node, whose outputs were incorrect or collapsed.[^bio] Completing the computation did not establish a correct structural prediction.

This specifies two separate achievements: the scale of computation that can be executed, and the quality of what it produces. Progress on the first can coexist with failure on the second.

Evaluations should consequently retain separate entries for cost and answer quality. An exact-output requirement cannot be assessed with a speed figure that permits numerical differences. A correct-structure requirement cannot be assessed by token capacity alone. This is the first axiom applied to an actual research report.

![Four separately assessed tasks: generate a candidate, check the statement, explain the important steps, and handle changed conditions.](/assets/img/articles/aei-v4-evidence-tasks.webp){: width="1200" height="1380" }
_Figure 2. Each capability has its own materials and tests. Arrows indicate that later work can use earlier outputs, not that success automatically passes from one stage to the next._

<span id="s11"></span>

## Fourth consequence: publication rules require information
{: #norms }

Mathematical correctness is one criterion. Whether a manuscript may be labeled “verified” also depends on publication rules.

On September 29, 2026, the Advisory Group on Mathematics and Artificial Intelligence published recommendations covering formalization status, provenance, attribution, and support for human understanding. These are scholarly norms, not ethical theorems deduced from model performance.[^agmai]

Once a norm is specified, however, its informational requirements can be examined.

Suppose a publication rule permits the label “formalized” only when a valid proof corresponds to that version's statement. A system that compresses “matching proof” and “proof of another version” into the same status label cannot guarantee a correct publication decision from that label alone.

Let $$A_N(x)$$ be the actions allowed by a norm in situation $$x$$. A system seeing only record $$z$$ can choose an action guaranteed to comply in every possible situation only if:

$$
\bigcap_{x:r(x)=z} A_N(x)\ne\varnothing.
$$

**Proposition 4. If situations sharing a record have no commonly permitted action, the system must obtain distinguishing information, change its available actions, or revise the norm before guaranteed compliance is possible.**

A rule allowing “pending verification” may provide a common action without immediate access to all details. The informational impossibility can arise when the system must also make an immediate affirmative judgment.

Normative demands thus require a further design check: a system held responsible for a distinction needs a way to observe it. Passing only an aggregate score downstream while demanding judgments about versions, grounds, and responsibility builds the failure into the process.

<span id="s5"></span><span id="s12"></span>

## Fifth consequence: preserving evidence preserves future questions
{: #future }

OpenAI's revision records retain withdrawal notices and routes to older manuscripts.[^history] A reader asking for today's manuscript count may not need them. A future researcher asking which step changed may have no adequate substitute.

The value of a record cannot therefore be measured only by current answer accuracy.

A small decision model makes the issue explicit. A detail is not needed today, but will be queried later with probability $$\lambda$$. Preserving it now costs $$s$$. Otherwise, a reliable source will supply it later for cost $$c$$. Assume later retrieval answers correctly and delay causes no additional loss. Expected costs are:

$$
C_{\mathrm{save}}=s,\qquad C_{\mathrm{retrieve}}=\lambda c.
$$

The first is preservation now; the second is retrieval if needed. **Proposition 5. Among these two policies and under these assumptions, preserving now is strictly cheaper if and only if** $$s<\lambda c$$. This is a conditional result, not a prescription to retain all raw data forever.

If the future source may disappear, retrieval is no longer equivalent to preservation. The model then needs a loss for unavailable answers. Privacy restrictions can also prohibit retention or require additional safeguards and costs. Those conditions cannot be omitted and then settled by the original formula.

**The resulting philosophical proposal is to include revisability in the assessment of understanding.** Two systems may give the same answer today, while only one retains traceable grounds. A withdrawal or a new question may expose a large difference between them.

Longer evaluations can detect what a short score hides. A useful summary should state the purposes it preserves, the follow-up questions it sacrifices, and whether omitted evidence remains recoverable.

<span id="s13"></span><span id="s15"></span>

## Sixth consequence: revision must follow dependencies
{: #philosophy }

The three OpenAI withdrawals were not merely three unrelated error labels. The revision record identifies a defect affecting a construction used by other manuscripts. This suggests another formal question: after evidence changes, which conclusions retain proof support?

Represent a conclusion as a node, connected to the premises and lemmas used to establish it. An acceptable proof requires valid inference steps and remaining assumptions that meet the assessment's acceptance conditions.

**Proposition 6. When a necessary supporting premise loses its accepted status, every proof that depends on that premise loses that justification. A conclusion with an independent valid proof can retain its support.**

This does not say that every downstream conclusion is false. A dependency graph identifies arguments requiring review. If a conclusion has another unaffected valid proof, failure of one route does not remove every ground for it. Without dependency records, a system may struggle to identify reliably which answers need revision.

This supplies a concrete research task: measure whether AI can identify affected derivations after a lemma is withdrawn, retain conclusions with independent support, and avoid continuing to cite obsolete versions.

The proposed assessment of understanding now includes producing results, giving grounds, handling changes, and withdrawing claims whose support has failed. These capabilities can be measured separately.

The mathematical propositions are deductions under explicit conditions. Including the corresponding capabilities in an account of understanding is a philosophical proposal. The former invite proof checking; the latter invite objections about what the proposal may omit, including explanation, intentionality, or subjective experience.

Even without agreement on a complete account, several poor arguments can be rejected. Authorship cannot replace content checking. One correct answer does not establish transfer. A whole process's performance cannot be assigned to one component without examining contributions. Executable scale cannot stand in for correctness.

<span id="s14"></span>

## Three experiments that can actually be designed
{: #experiments }

Axiomatization should lead to executable research designs. The following are proposals based on the available materials; this article does not report having run them.

**Remove different materials and measure which capabilities disappear.** Prepare versions containing only conclusions, full papers, and papers plus dependency and revision records. Hold the model and budget constant. Separately test status recognition, explanation of assumptions, error location, and changed conditions. A correct answer may already be present in model parameters: absence from the prompt does not establish absence from the system. Newly constructed controlled tasks may be needed, clearly distinguished from the published research.

**Change the evidence.** Supply a collection of supported conclusions with explicit dependencies, then withdraw a lemma. Penalize both keeping proofs whose only support has failed and indiscriminately withdrawing conclusions with independent proofs. This measures revision rather than a habit of always asking for more checks.

**Compare research processes at equal cost.** One process concentrates on generating candidates; another reserves resources for verification, explanation, and version maintenance. Compare outputs that meet a predefined standard for further research, not manuscript count alone. Include outside tools and human work in the budget.

These experiments do not independently settle consciousness. They address specific questions: which records support which abilities, which errors require additional evidence rather than computation, and which research processes produce work that remains usable after challenge.

<span id="s16"></span>

## Claims of understanding should become as concrete as the results
{: #return }

The new 3SUM and APSP results make “AI only rearranges existing answers” inadequate as a description of current research. OpenAI's release and withdrawals show why production volume, proof status, and revisability need separate records. Biomolecular-modeling results show why greater speed and scale must still be evaluated against the original correctness requirement.

Understanding need not require complete possession of the world. It does require a stated scope: the questions covered, the evidence available, the resources used, and the response when evidence changes.

Axiomatization connects these requirements. Retained information limits follow-up questions. Algorithms determine the cost of using it. Publication rules determine which distinctions cannot be omitted. Dependency records make targeted correction possible.

New capabilities deserve recognition and precise questions. As AI supplies methods researchers had not found, understanding needs criteria that can follow those results into their proofs, applications, and revisions.

<span id="s17"></span>

## Sources and version note
{: #references }

Sources were checked on **October 8, 2026**. Recent results are described from original papers, institutional reports, and revision records. This article does not independently rerun every Lean proof or treat a preprint or institutional report as completed external peer review. Its propositions and experiments are analyses under stated assumptions, without a claim of priority for the underlying mathematical observations. The conditions and limitations are stated in the article; the proposed experiments have not been performed.

[^algorithm]: Josh Alman and Virginia Vassilevska Williams, [*Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs*](https://arxiv.org/abs/2610.06783), arXiv:2610.06783v1, October 5, 2026. The article uses the abstract's bounds in its stated integer regimes. Theorem 22 gives the stronger APSP exponent 2.99942. These are not measured practical runtimes.
[^method]: The paper's [Acknowledgments and Methodology](https://arxiv.org/html/2610.06783v1) describes discovery, human contributions, and subsequent Lean certification, with a link to [anthropics/formal-math — 3sum-apsp](https://github.com/anthropics/formal-math/tree/main/3sum-apsp). The account here does not characterize the complete project as human-free.
[^release]: OpenAI, [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/), October 6, 2026.
[^catalogue]: OpenAI, [math repository](https://github.com/openai/math) and [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md). The initial 722 manuscripts and 372 families must be read alongside the current 719-manuscript count and withdrawal record.
[^history]: OpenAI, [history.md](https://github.com/openai/math/blob/main/history.md), October 7, 2026 revision entry. Source for withdrawals, revisions, retained older versions, and the 300/719 formalization figure.
[^bio]: Anthropic, [How Claude is uplifting biomolecular modeling](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling), September 17, 2026. Publisher-reported results; identical outputs and permitted numerical differences are different evaluation conditions. The very large runs used one eight-GPU B300 node, not one GPU.
[^agmai]: Advisory Group on Mathematics and Artificial Intelligence, [Responsible Release of AI-Generated Mathematics](https://agmai.org/general-sep29/), September 29, 2026. These publication recommendations do not certify individual results.
