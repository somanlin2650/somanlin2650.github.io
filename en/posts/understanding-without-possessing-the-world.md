---
layout: post
title: "Understanding Without Possessing the World: AI and an Axiomatic Account of Finite Inquiry"
date: 2026-10-08 11:30:00 +0800
last_modified_at: 2026-10-08 13:53:14 +0800
lang: en
permalink: /en/posts/understanding-without-possessing-the-world/
alternate_url: /posts/understanding-without-possessing-the-world/
categories: [AI, Philosophy]
tags: [AI, Epistemology, Axiomatic Philosophy, Understanding, Representation, Revisability, No View Is the Whole]
description: "AI separates cognitive achievement from familiar human forms of thought. Starting with a proof and a ledger stripped of detail, three axioms expose limits on information, error detection, ethical decisions, and future revision—and make inquiry itself a subject of design."
toc: true
comments: true
math: true
---

<span id="s1"></span>

## Cover the author's name
{: #proof }

Imagine a geometry proof on a desk. We cover the author's name and check the premises, the auxiliary lines, and each inference. Everything holds. Now we uncover the name. The author is an artificial intelligence system.

Which step needs checking again?

We might ask whether it copied the answer, whether it can handle a slightly altered problem, or whether our inspection missed a mistake. Each suspicion points to something we can investigate. Learning that the author is not human does not, by itself, invalidate an inference.

This small thought experiment has a real counterpart. AlphaGeometry, published in 2024, combines a neural model that proposes geometric constructions with a symbolic engine that carries out deductions, producing proofs that can be checked. It demonstrates a specific ability, without settling questions about consciousness, experience, or general intelligence.[^ag] It does, however, separate two questions that are easily confused: what makes a result valid, and how closely the process that produced it resembles human thought.

“It can do it, but it doesn't understand.” There may still be something to this objection. Reciting a proof differs from explaining why a particular auxiliary line helps. But we now owe an account of the difference. Can the system handle changed conditions? Can it locate the step that fails? Does it grasp a relation between the reasons and the conclusion? If the missing property is subjective experience, that claim should be stated in its own right. It should not silently erase an ability already demonstrated.

AI makes me want to ask something we ask less readily of ourselves: when did we earn the certificate of understanding that we demand from another kind of cognitive system?

We have not moved the world into our heads. Learning a formula requires ignoring much that does not matter to the present question and keeping a relation we can use again. Maps, concepts, programs, and institutions work in much the same way. Sometimes these arrangements help us get things right. Sometimes they keep errors out of sight for years. Their omissions do not make every achievement an illusion; their successes do not make the omitted details cease to exist.

The change I propose is to treat “understands” as a substantive claim about ability, open to further questions. What is understood, which variations can be handled, what warrants the result, and what resources are needed should belong to the claim itself. Possessing the whole world may be unnecessary for understanding. Once we drop that requirement, though, we need something more demanding than “whatever works.”

<span id="s2"></span>

## What the ledger no longer records
{: #ledger }

Leave AI aside for a moment. Consider a tiny ledger recording the resources held by two people, in arbitrary units. One possible entry is forty and sixty. Another is zero and a hundred. The total is the same. So is the mean.

If the only question is the mean, either entry can be replaced by “fifty.” The summary is correct. But suppose the next question is whether anyone has less than twenty. The summary cannot answer it.

| Detailed entry | Mean | Anyone below twenty? |
| :-- | --: | :-- |
| 40, 60 | 50 | No |
| 0, 100 | 50 | Yes |

The trouble begins when the detail is deleted. If the original record is destroyed and the past situation cannot be reconstructed, thinking harder about fifty will not reveal which entry produced it.

There is no mysterious cognitive barrier here. Everything is on the page: one visible record is compatible with two different correct answers.

Machine learning presents related cases. A model can perform well under a specified distribution and scoring rule without uniquely identifying the entire mechanism that generated the data. Finite tests establish less still: a few successful trials do not guarantee success throughout the intended range.[^uml] This does not establish that the human brain is a particular kind of machine-learning model. It does expose a shared problem. We often test what a retained representation can do, while paying less attention to the questions it has made impossible to answer.

This is the sort of problem I want an axiomatic approach to philosophy to reach. After writing down the axioms, we should be able to say which ambitions cannot be met under those conditions—and which condition must change to make them possible.

<span id="s3"></span>

## What cannot be obtained for free
{: #axioms }

The model below addresses part of finite inquiry. It does not attempt to derive the world from a few symbols. Let $$X$$ be the set of situations admitted in a particular study and $$Q$$ the questions to be answered. Each question $$q$$ has an answer rule $$q(x)$$. The inquirer initially receives a record $$z=r(x)$$, where $$r$$ may describe sensing, summarizing, or encoding information in memory. For transparent proofs, take these sets to be finite.

Those are definitions. The model adopts three axioms.

**Axiom A1: Within an assessment, the criterion does not change with the answer being assessed.** When asked for the mean, the answer is determined by the ledger. An inquirer cannot rename some easier quantity “the mean” and claim to have solved the original problem. A criterion can be challenged. Changing it establishes a different assessment; it does not retroactively change the earlier result.

**Axiom A2: Available reasoning depends only on accessible information.** If two situations provide exactly the same observable record, the system cannot branch on their hidden difference before receiving further evidence. It may randomize, deliberate, or seek assistance. Its random seed does not foresee the answer. If an assistant brings relevant knowledge, that counts as an addition to the information available.

**Axiom A3: Acquiring and using information share one resource account.** Retaining detail, rereading data, calling tools, searching for a proof, and checking a result count toward the task's stated limits. Each example specifies whether it concerns worst-case time or memory, or an average cost. These constraints are not interchangeable.

A1 separates being correct from declaring oneself correct. A2 excludes knowledge with no source. A3 prevents us from describing an inquirer as finite while supplying it with a free, omniscient assistant. None of these commitments is exotic. Axiomatization makes the argument answer to them, rather than merely acknowledge them.

Being part of the world does not, by itself, prove that an inquirer cannot understand it. A one-bit world might contain an inquirer able to retain everything needed for the relevant questions. An information limit requires assumptions about capacity and questions. A computational limit requires assumptions about the problem to be computed. Finitude, embeddedness, and failure are related, but one cannot be substituted for another.

The axioms also do not tell us which questions to ask or which social arrangements to pursue. When norms and revision enter the argument, their additional commitments will be stated. Hiding those choices inside the word “rationality” would make a dispute less visible without resolving it.

<span id="s4"></span>
<span id="s6"></span>
<span id="s7"></span>
<span id="s9"></span>

## The distinctions understanding needs
{: #distinctions }

Return to the ledger. Put the relevant questions together. Treat two situations as equivalent, written $$x\sim_Q x'$$, when they give the same answer to every question in $$Q$$. This does not make them the same world. It means the present task need not distinguish them.

We now have an exact criterion. Every question in $$Q$$ can be answered correctly from $$r(x)$$ alone if and only if

$$
r(x)=r(x')\quad\Longrightarrow\quad x\sim_Q x'.
$$

Necessity is immediate. If a record merges situations whose answers differ, A2 prevents the system from separating them without further information. Sufficiency is simple too. If every situation sharing a record has the same answers, we can fill in an answer table for that record. This proves the table exists. Whether there is room to store it or time to consult it is a further question under A3.

The minimum number of record states is therefore the number of classes into which $$\sim_Q$$ divides $$X$$. If there are $$m$$ classes, a fixed-length binary encoding needs at least $$\lceil\log_2 m\rceil$$ bits. This counts the record alone, excluding the decoder, program, and execution time.

![The same four situations are grouped differently when asked for a, for b, or for both: the tasks require two, two, and four distinguishable record states respectively.](/assets/img/articles/aei-v2-query-partitions.webp){: width="1600" height="1050" }
_Figure 1. Questions determine the distinctions that must survive. This is an exact classification in a finite example, not an estimate of human memory capacity._

One consequence concerns concepts. A concept can omit details, but it cannot omit a distinction required by the questions it claims to answer. “Mean” is a good concept. Using it to decide whether a distribution leaves someone behind exceeds its capacity. A concept sometimes fails because the question has changed while the record has not.

Understanding need not fall along a single scale, either. A system retaining only $$a$$ and one retaining only $$b$$ each store one bit. The first is better when asked for $$a$$; the second is better when asked for $$b$$. Neither is unconditionally superior. A score that ranks them must assign weights to the questions. Change those weights and the ranking may change.[^blackwell]

Allowing errors does not remove the information constraint. Let $$a$$ and $$b$$ be independent fair bits. Retain only $$a$$, then ask for $$b$$. No amount of computation can reduce the error rate below one half: conditional on either observed value of $$a$$, zero and one remain equally likely values of $$b$$.

Having ten systems discuss the problem does not automatically change this. If all their relevant information consists of $$a$$, the discussion still cannot distinguish the values of $$b$$. Give one of them access to $$b$$, however, and the situation changes at once. Access to evidence makes the difference.

This also means that giving several AI models the same prompt does not establish that they have the same information. Their prior knowledge, tools, and memories may supply different clues. A single model may derive a consequence after additional computation that it failed to derive before. A2 rules out creating absent information; it does not rule out progress through thought.

Questions about why things happen encounter the same issue. Let $$U$$ be a fair bit. In model A, $$X=U$$ and $$Y=X$$. In model B, $$X=U$$ and $$Y=U$$. Ordinary observations always show $$X=Y$$ in both. But forcibly setting $$X$$ to zero makes $$Y$$ zero in model A, while in model B, $$Y$$ continues to depend on $$U$$. The causal accounts agree observationally and separate under intervention.[^pearl]

Without intervention data or an additional assumption excluding one model, more observations of the same kind will not decide between them. Argument can test their internal coherence. Finding out which account applies requires a way of eliciting a different response from the world.

<span id="s18"></span>

## The missing step in “we can fix it later”
{: #diagnosis }

Revisability can sound easy: use a simplified model for now, and collect more data when it goes wrong.

Who tells us that it has gone wrong?

Suppose a system answers from its record. In one situation the answer is correct; in another it is mistaken. If both situations leave exactly the same record, an alarm reading only that record must give the same verdict in both. It can flag both or pass both. It cannot light up only for the mistake.

The proof uses A2 alone. “Is this answer wrong?” is another question. When the record merges correctness with error, self-checking encounters the same barrier as the original task.

This is more specific than saying a model may not know what it does not know. It identifies an impossible combination: without any distinguishing clue, an alarm cannot avoid both missed errors and false alarms. Asking the system to be humble will not secure both benefits.

The system may still recognize that its record is insufficient and request checking in every case. Recognizing a risk differs from identifying exactly which answer is mistaken.

We can also calculate a cost. Consider another constructed example. The answer is a hidden bit $$b$$ with a one-in-ten probability of being one. The system has no clue correlated with $$b$$ and ordinarily answers zero. At cost $$c$$, it can query the exact answer. It must decide whether to query before submitting its final answer.

Let $$\rho$$ be the fraction of cases queried. Since the information available before querying is independent of $$b$$, the system cannot preferentially select the one-in-ten cases. Among the unqueried cases, one in ten will still be wrong. Thus

$$
\text{residual error}=0.1(1-\rho),\qquad
\text{expected query cost}=c\rho.
$$

Reducing the error rate to one percent requires querying at least ninety percent of cases. Randomly querying nine out of ten achieves that bound. “Intelligent selection” without relevant clues cannot do better.

![With no informative clue before querying, the minimum error falls linearly from ten percent to zero as the query rate rises from zero to one hundred percent. A ninety percent query rate is needed for one percent error.](/assets/img/articles/aei-v3-repair-frontier.webp){: width="1600" height="1000" }
_Figure 2. A query bound without informative clues. The values follow from the example's assumptions, not measurements of current AI systems. Additional clues would require a different bound._

A revisable system therefore needs more than a retry button. Through what signal will a mistake become visible? Who can supply that signal? How long does checking take? If no signal arrives, does the system pause, sample cases, or carry on?

An organization that discards complaint records while retaining only processing totals may lose the ability to identify what needs improvement. This is an institutional analogy, not an application of the numerical one-in-ten assumption to society. It preserves the relevant question: evidence needed for revision can be discarded before revision begins. External observation, discussed in [“When AI Cannot See Its Own Hypoxia”](/en/posts/when-ai-cannot-see-its-own-hypoxia/), now has a specific job.

<span id="s8"></span>
<span id="s10"></span>

## Even if the rule is short
{: #laws }

Keeping the information intact still does not settle what we can understand.

Imagine a world of black and white cells. A cell's next color depends only on itself and its two neighbors. Three bits admit just eight combinations, so the entire update rule fits in a small table. Rule 110 is one such rule.

Cook proved that Rule 110 supports universal computation under suitably encoded initial configurations.[^cook] A procedure that always halted and decided whether the computation encoded in any such configuration would halt could therefore solve the general halting problem. No such procedure exists.

This undecidability result uses an unbounded family of configurations. It does not follow directly from the fixed finite model used earlier.

![The eight local update cases of Rule 110 and a finite sequence of black-and-white cells generated from a specified seed.](/assets/img/articles/aei-rule110.webp){: width="1600" height="1000" }
_Figure 3. The full local rule appears above a finite illustrative evolution. The image does not prove universality, and the depicted seed is not the full encoding used in Cook's simulation of arbitrary computation._

This does not make every Rule 110 pattern difficult, and it does not establish that the physical universe is such a system. Questions about specified finite regions and finite times can be handled in finitely many steps. The counterexample is enough: a short rule need not provide a feasible solution to every general question formulated about it. Computation can obstruct us even when information is complete.

“Finding the final laws” thus separates into at least two achievements: knowing how a world updates, and being able to answer the questions we ask of it. The first does not automatically deliver the second. This also explains why a better concept can improve our abilities without adding information. A table prepared in advance, a suitable coordinate system, or a completed derivation packaged for reuse may make an otherwise intractable task manageable. Preparation has a cost. Whether it pays depends on how often the result will be used.

This is another aspect of [“You Don't Have to Rediscover the World”](/en/posts/you-dont-have-to-rediscover-the-world/): we inherit conclusions and some of the computational labor already spent on reaching them.

Abstraction has another condition to meet. Suppose a detailed state $$x$$ evolves under a deterministic rule $$F$$ and we retain only a summary $$r(x)$$. A deterministic next-step rule on summaries exists if and only if

$$
r(x)=r(x')\quad\Longrightarrow\quad r(F(x))=r(F(x')).
$$

Otherwise, one present summary can lead to two different future summaries, so it cannot determine the next step alone. For example, let the detailed rule swap two bits: $$(a,b)\mapsto(b,a)$$. If the summary retains only the first bit, a current zero may become either zero or one, depending on the omitted second bit.

This gives us a test for some claims that a higher-level description can operate on its own. When the condition fails, we might add variables, retain history, or seek probabilistic predictions instead. It does not settle whether macroscopic objects are “real,” nor reduce every kind of emergence to forgetting. It settles a narrower question: can this summary perform the predictive work assigned to it?

<span id="s11"></span>

## Who decides which differences matter?
{: #norms }

We can now return to the ledger that retains only the mean.

If the task is merely to report the total, deleting detail may be harmless. But suppose an institution adopts this rule: initiate an additional allocation if anyone has less than twenty; otherwise, do not. Forty and sixty now demand a different action from zero and a hundred. A record containing only the mean cannot comply in both situations.

Mathematics has not established that anyone below twenty ought to receive assistance. That is an additional, contestable norm adopted for the example. Mathematics shows that once we adopt it, a particular way of deleting information conflicts with compliance.

We can state the condition more precisely. Let $$A_N(x)$$ be the set of actions allowed by norm $$N$$ in situation $$x$$. A guaranteed permissible action can be chosen from summary $$z$$ alone if and only if

$$
\bigcap_{x:r(x)=z}A_N(x)\ne\varnothing
\quad\text{for every possible }z.
$$

The reason is that the same summary must lead to an action permitted in every compatible situation. If the intersection is empty, each choice fails somewhere. If it is nonempty, we can select a member. This addresses the existence of an information-based choice; affordability remains a further test.

The formulation also prevents an overstatement. Two situations need not always be distinguished. If “defer and investigate” is allowed in both, it can be chosen without knowing which situation obtains. That escape closes only if investigation is forbidden, too late, or beyond the available budget.

The resulting demand is considerably narrower than “collect more data.” Under this particular rule, a reliable indicator of whether anyone is below twenty may suffice. Names, addresses, and complete life histories need not be retained. If the task also requires identifying the recipient of an allocation, the information requirement changes again. Privacy constraints can themselves be included among the conditions on permissible actions. If the requirements cannot jointly be met, the conflict should be exposed rather than concealed by an algorithm.

Ethics can therefore reach upstream into data design. Adding a fairness score to a completed model's outputs may come too late: the distinctions needed to assess a harm may already have disappeared from the fields. For [a morality we can revise](/en/posts/a-morality-we-can-revise/), this creates a further difficulty. Agreement on a better norm tomorrow does not guarantee that yesterday's decisions can be reassessed. The necessary evidence may no longer exist.

A promise to revise can be far removed from the conditions that make revision possible.

<span id="s5"></span>
<span id="s12"></span>

## The same answers, different futures
{: #future }

Two systems currently use summaries and answer the same test questions correctly. One retains access to the original records; the other has permanently deleted them. Their present scores are identical. A new question exposes the difference.

We can calculate that difference, but cannot assume that keeping options open is always worth the cost.

Take independent fair bits $$a,b$$ again. Today's question asks for $$a$$. Both systems retain it and have not yet read $$b$$. There will be one future question: with probability $$\lambda$$ it asks for $$b$$, and otherwise for $$a$$. Before learning which question will arrive, a system can pay $$s$$ to acquire and store $$b$$. If it retains later access, it may instead pay $$c$$ to read $$b$$ only when asked for it. Otherwise it must guess. A wrong answer costs $$L$$; all costs have been converted to common units under specified weights.

After excluding fixed processing costs common to all three approaches, their expected additional costs are:

| Approach | Expected additional cost |
| :-- | --: |
| Neither acquire early nor query later; guess on the new task | $$\lambda L/2$$ |
| Acquire and retain $$b$$ in advance | $$s$$ |
| Wait for the question and query only when necessary | $$\lambda c$$ |

Within these available operations, the minimum additional cost is

$$
V=\min\{\lambda L/2,\ s,\ \lambda c\}.
$$

The system is not allowed to peek at the future question. The early acquisition decision precedes both seeing $$b$$ and learning the question; a later query follows the question. With no other relevant clues, random mixtures of these policies produce weighted averages of their costs and cannot improve on the minimum.

If later access has been closed, the $$\lambda c$$ option disappears. An unused channel already affects the cost at which the system can respond to what comes next.

![Expected costs of early retention, querying on demand, and guessing under a specified future-task probability and cost model. The lowest attainable cost changes when later access is removed.](/assets/img/articles/aei-v3-option-cost.webp){: width="1600" height="1100" }
_Figure 4. Wrong-answer loss L = 1, early acquisition and retention cost s = 0.12, later query cost c = 0.2. The curves are formula outputs. Different task distributions, costs, or available operations can change the preferred policy._

Revisability now has a content beyond attitude. After a question changes, which operations for collecting evidence, changing representations, and checking results can actually be performed? Who is authorized to start them? A file existing somewhere does not mean this system can read it. Read permission does not ensure it can be retrieved before a deadline.

The formula also declines to guarantee that retaining everything is best. Rare new questions, expensive memory, or cheap, reliable retrieval produce different choices. In practice, even $$\lambda$$ may be unknown. We can compare assumptions or specify a worst-case loss we are prepared to bear. We cannot pass off an uncertain future as a known distribution.

The change concerns evaluation. Today's answer sheet does not describe the whole of a system's cognitive capacity. Part of that capacity resides in what it can actually do when change becomes necessary.

<span id="s13"></span>
<span id="s15"></span>

## Where philosophy can work
{: #philosophy }

At this point, saying that philosophy should study understanding has acquired a different content.

What a ledger deletes, what a model can read, which counterexamples a test admits, and who may challenge an institution are usually treated as conditions fixed before the real work begins. Yet the arguments above show how success or failure can be determined at that earlier stage. Working harder within the given conditions may leave even the source of a problem invisible.

I propose making those conditions part of philosophy's work: the questions we formulate, the concepts we use, the distinctions we preserve, the rules of inference, the procedures of checking, and the ways people can revise all of these. They can be analyzed separately. They must eventually fit together in a process of inquiry that can operate.

There are predecessors. Carnap's work on explication asks us to construct clearer, usable concepts, rather than confining ourselves to the analysis of ordinary words.[^carnap] Peirce's discussion of the fixation of belief gives an important place to methods of inquiry and constraints beyond individual preference.[^peirce] Neither contextual understanding nor the idea that philosophy can design concepts is a discovery made here.

The attempted contribution is a connected set of checks. A concept's range depends on the distinctions it preserves. A promise of correction depends on whether failure can become visible. A norm's implementability depends on whether merged situations admit a common permissible action. Future capacity depends on executable procedures for retrieval and revision. Most of the mathematical results have established relatives. Applying them together in a philosophical proposal will be worthwhile if it reveals conflicts we would otherwise miss and helps us build better arrangements.

I call this direction Axiomatic Embedded Inquiry, or AEI. The name belongs to a revisable research program. It need not announce a completed unified theory of philosophy.

One choice in this proposal cannot be supplied by a theorem: I favor evaluating understanding publicly through warranted abilities, their scope, and practicable revision. This is a claim about concepts and methods. The preceding results expose constraints that the proposal must face; they do not prove that everyone must accept this use of “understanding.”

Someone may object that an answer table could satisfy the earlier tasks without understanding anything. I agree that this identifies a gap. Information sufficiency asks whether correct answers can be recovered. We may additionally require tracking consequences under changed conditions, separating causes from correlations, reconstructing reasons, or handling unmemorized cases within reasonable cost. Those requirements need separate assessment. A high score cannot stand in for them. Experience and consciousness lie outside the finite model; neither their presence nor their absence follows from it.

Axiomatization does not end every dispute. It makes certain substitutions harder: presenting one success as complete understanding, treating undetectable mistakes as readily correctable, identifying a preferred score with truth, or treating unavailable information as something effort alone can supply.

This changes what a philosophical advance might look like. It may consist in proving that familiar demands cannot all be satisfied together, then identifying the information that must be retained, the cost that must be paid, or the norm that must be openly revised if we still intend to achieve the aim.

<span id="s14"></span>

## Give the proposal a chance to fail
{: #experiments }

These ideas can be tested experimentally. The experiments should leave room for results that disappoint our expectations.

The first separates missing information from inadequate computation. Give two groups the same questions and total resource allowance. One can only deliberate over data with a crucial field removed; the other can spend some of its allowance retrieving that field. Add another task family in which all information is present but more computation is required. Extra evidence should help the first kind of difficulty, and extra computation the second. Where the data-generating and deletion procedures genuinely remove all answer clues, thought alone should not break the information bound. If it appears to do so, first check for leakage or an inapplicable bound.

The second evaluates alarms. Counting admissions of uncertainty is insufficient. Measure missed errors, false alarms, and the cost of reducing both. A control group without relevant clues can be compared with the bound above. Introduce measurable clues, then ask whether selective checking actually saves resources. This distinguishes cautious language from diagnostically useful information.

The third delays revealing a new task family. First bring systems to comparable performance on the original task. Then compare systems with access to original records, systems left with summaries alone, and systems retaining different summaries. Charge for storage, retrieval, coordination, inference, and verification as they adapt. Task distributions and resource differences must be declared; otherwise, apparent revisability may simply reflect more data or more time.

These are proposed studies. The figures and numbers in this essay come from finite examples with explicit assumptions. They are not measurements of any deployed agent.

An implementation would not need an allegedly omniscient supervisor for every failure. It could ask for a checkable diagnosis: missing evidence, excessive computational demand, conflicting criteria, or an unresolved cause. The diagnosis itself needs evaluation. Unclassified cases still need sampling or escalation. Whether the arrangement earns its cost depends on the errors it prevents and the resources it consumes.

<span id="s16"></span>

## Put the name back
{: #return }

Now put the author's name back on the geometry proof.

The name still matters. We ask where the data came from, who is responsible, and how much trust is warranted. Knowing how a system fails affects how we allocate checking effort. But a valid proof does not lose its validity. Nor can a familiar, recognizably human author make an invalid inference sound.

We can hold our own understanding to the same demands. Being able to answer deserves recognition. Giving reasons, surviving changed conditions, and deciding when to check on the basis of evidence and risk are further abilities to acquire. Different bodies, tools, and arrangements of cooperation may realize them. They need not all resemble the processes familiar from human introspection. This is part of the space opened by [“From Reaction to Heterogeneous Rationality”](/en/posts/from-reaction-to-heterogeneous-rationality/).

AI has not established that thousands of years of human inquiry were mistaken. It does remove a convenience: familiar human forms of cognition can no longer be assumed to mark the natural boundary of cognitive achievement. An axiomatic study of finite inquiry can then ask what follows. If understanding does not require a complete internal copy of the world, which abilities should qualify, and what must we pay for the standards we choose?

One score sheet will not finish the answer. The ledger can still correctly report fifty today. Whether it can tell us who needs help tomorrow depends on what we keep now.

<span id="s17"></span>

## Notes and references
{: #references }

[^ag]: Trinh, T. H. et al. (2024), “Solving olympiad geometry without human demonstrations,” *Nature* 625, 476–482. [Paper](https://www.nature.com/articles/s41586-023-06747-5). Cited for its neural-symbolic method and checkable geometry results, not as evidence of general understanding or consciousness.
[^uml]: Shalev-Shwartz, S. & Ben-David, S. (2014), *Understanding Machine Learning: From Theory to Algorithms*. [Authors' textbook](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf). Background for distinguishing distributional performance, evidence from finite samples, and identification of a generating mechanism; no claim that all learning is lossy compression.
[^blackwell]: Blackwell, D. (1953), “Equivalent Comparisons of Experiments,” *Annals of Mathematical Statistics* 24(2), 265–272. [DOI](https://doi.org/10.1214/aoms/1177729032). The value of information across decision problems has an established theory. The essay's one-bit example is an elementary construction, not a statement of the full theorem.
[^pearl]: Pearl, J. (2009), “Causal inference in statistics: An overview,” *Statistics Surveys* 3, 96–146. [Author's paper](https://ftp.cs.ucla.edu/pub/stat_ser/SS-2009-57-Sup.pdf). The two-model example illustrates that observational agreement need not imply agreement under intervention.
[^cook]: Cook, M. (2004), “Universality in Elementary Cellular Automata,” *Complex Systems* 15(1), 1–40. [Original paper page](https://www.complex-systems.com/abstracts/v15_i01_a01/). Universality involves appropriate encodings and background configurations; arbitrary finite patterns are not claimed to have the same difficulty.
[^carnap]: Carnap, R. (1950), *Logical Foundations of Probability*, Chapter I, §§2–3, on the task and requirements of explication. [Scan](https://www.fitelson.org/confirmation/carnap_logical_foundations_of_probability.pdf). Cited as a precursor in concept construction, not as the source of the essay's entire formal model.
[^peirce]: Peirce, C. S. (1877), “The Fixation of Belief,” *Popular Science Monthly* 12, 1–15. [Transcription](https://www.peirce.org/writings/p107.html). A precursor concerning methods of inquiry and external constraints.
