---
layout: post
title: "Understanding Without Possessing the World: Axiomatizing Inquiry After AI"
date: 2026-10-08 11:30:00 +0800
last_modified_at: 2026-10-08 19:59:10 +0800
lang: en
permalink: /en/posts/understanding-without-possessing-the-world/
alternate_url: /posts/understanding-without-possessing-the-world/
categories: [AI, Philosophy]
tags: [Artificial Intelligence, Epistemology, Axiomatization, Understanding, Machine Learning, Mathematics, Revisability]
description: "AI finds methods people had not found, without ever possessing the world's true structure. Starting from approximation in machine learning, the essay takes apart a leap hidden for two centuries, from “truth exists” to “a finite knower will possess it,” and derives shared conditions for concepts, science, machine learning, ethics, and philosophy itself from three foundational and three operational axioms."
toc: true
comments: true
math: true
---

<span id="s1"></span>

## Cover the author's name
{: #proof }

On October 5, 2026, Josh Alman and Virginia Vassilevska Williams published an algorithms preprint giving an $$O(n^{1.9992})$$ algorithm for 3SUM on polynomial-size integers and an $$O(n^{2.9995})$$ bound for all-pairs shortest paths, or APSP, on directed graphs with polynomially bounded integer weights. The results refute the corresponding 3SUM and APSP hypotheses.[^algorithm]

3SUM asks whether an input contains three numbers whose sum is zero; −4, 1, and 3 form a solution. With a few numbers the task is easy. The question is how the work grows with the input. The change from an exponent of 2 to 1.9992 looks small; its significance is that the reduction is a fixed positive amount, so the asymptotic saving keeps growing with the input. Constants, input regimes, and implementation costs can still make the new method slower at ordinary scales. The breakthrough concerns conjectured asymptotic barriers. It does not overturn a proved lower bound, and it does not establish an immediate practical speedup.

Cover the author line and check only the premises, the construction, and each step. The proof holds. Now uncover the name. The paper's methodology credits Claude with discovering the key algorithm during a research session that received no further human input after the initial task; human authors subsequently organized, strengthened, and extended the work and take responsibility for the paper; Lean formalization of the principal results followed completion of the manuscript.[^method]

Which step needs checking again?

We may ask whether the system copied an answer, whether it can handle a slightly altered problem, or whether our inspection missed a mistake. Each suspicion points to something that can be investigated. Learning that the author is not human does not, by itself, invalidate a valid inference.

What deserves a longer look is the system's situation. It learned from finite data, operates within finite resources, uses its own internal representations, and revises answers through reasoning and tools. It did not move the “true structure” of 3SUM into a machine, and it acquired no infallible claim to omniscience. It still did something human experts had not done in decades.

If a system that possesses no true representation can produce new mathematical discoveries, new algorithms, scientific reasoning, and conceptual analysis, then holding the real essence of a thing in one's mind is not a necessary condition for high-level cognition. The full weight of that sentence appears only once we see how such systems work.

## Machine learning never had f*
{: #approximation }

A basic supervised-learning setting runs as follows. Suppose the world contains some target relation $$f^*:X\to Y$$ that we would like to capture. Nobody has $$f^*$$ during training. What is available is a finite sample, a loss function $$\ell$$, and a distribution $$D$$ from which the data come. Learning searches for a model $$\widehat f$$ such that

$$
\widehat f\approx_{\mathcal C} f^*.
$$

The subscript $$\mathcal C$$ cannot be dropped. It names the situations and questions we care about, the tolerated error, and the available resources. The quantity of theoretical interest is the risk $$R_D(f)=\mathbb E_{(x,y)\sim D}[\ell(f(x),y)]$$; what can actually be computed is the empirical risk on a finite sample, and the gap between the two is governed by the conditions that learning theory studies.[^uml] Low average loss does not imply correctness at every input. A shift in the distribution can void an earlier guarantee. With noise, the “best prediction” is only the best decision relative to a distribution and a loss. Some learning problems do seek identification of true parameters; the point here is that successful performance does not universally require global identification.

This is how the most successful artificial cognitive systems work: no $$f^*$$, only approximation tested under explicitly stated conditions.

The next question is the entrance to this essay. If the most successful artificial cognitive systems have always worked this way, why are we reluctant to admit that human knowing may always have worked this way too?

Imagine three people entering the same city. One needs to change trains, one is looking for low ground likely to flood, and one is planning a walk. A transit map can straighten the tracks, enlarge the crowded center, and omit most streets; as long as station connections and transfers are right, the distortions do not get in the way. Hand it to the person investigating floods and the problem appears: the omitted elevation and drainage are exactly what that job needs. A map's purpose decides which distinctions deserve to be drawn, and once the purpose is stated, the map can be right or wrong. Learning a formula, using a concept, and following an institution belong to the same family of activities: ignore a great deal that is irrelevant to the present question, and keep a relation that can be used again.

Written down, the structure is $$R\approx_{\mathcal C}W$$: a representation $$R$$ preserves the usable structure of the world $$W$$ under stated conditions. This is an abbreviation that has to be unpacked into task error, evidence, and operating conditions. It does not posit an undefined “distance between a representation and the cosmos.”

## A leap hidden for two hundred years
{: #privilege }

In 1814, in his *Philosophical Essay on Probabilities*, Pierre-Simon Laplace wrote the passage later known as Laplace's demon. He imagined an intellect that, at one instant, knows all the forces that set nature in motion and the positions of all the things that compose it, and is vast enough to analyze those data; for such an intellect the movements of the greatest bodies and the tiniest atoms would fall under one formula, nothing would be uncertain, and the future, like the past, would lie open before its eyes. What is usually left out is the sentence that follows. The human mind, Laplace wrote, in the perfection it has achieved in astronomy, offers only a feeble idea of this intelligence, and all its efforts in the search for truth tend to bring it continually nearer to that intelligence, from which it will always remain infinitely removed.[^laplace] Laplace himself placed that vantage point beyond human reach. The picture nevertheless survived: truth is over there, the complete picture of the world is over there, and the highest task of knowing is to move step by step toward possessing it.

In September 1930 another scene pushed the same picture to its limit. From September 5 to 7 a conference on the epistemology of the exact sciences met in Königsberg. At the closing roundtable on the 7th, Kurt Gödel, aged twenty-four, remarked in passing that he could give examples of true but unprovable arithmetical propositions in the formal system of classical mathematics. Almost nobody present noticed; only John von Neumann followed up. The next day, September 8, in the same city, David Hilbert, about to retire, addressed the Society of German Scientists and Physicians on “Logic and the Understanding of Nature” and closed with the words later carved on his gravestone: we must know, we shall know. The ending was recorded again shortly afterward at the local radio station, and the recording survives.[^hilbert] What makes the coincidence worth remembering is that it shows two things holding at once: faith in complete knowledge can drive an entire discipline, and the assumption that faith rests on was, at that very moment and in that very city, being taken apart.

Written out, the assumption looks like this:

> **The world has a real structure ⟹ a finite knower will eventually possess a complete representation of it.**

The antecedent may well be true. The consequent never followed from it; it was always attached in secret. AI has not proved that truth does not exist, nor that all views are equal. What AI has done is to hold the following implication up to the light and let us see that it fails:

> **Successful cognition ⇏ possession of truth.**

The position of this essay is therefore not anti-truth. It rejects only the step from “truth exists” to “a finite inquirer will eventually possess it completely.” That step propped up the presumed status of humans as a special kind of knower: we may not know everything yet, but human reason stands on a road toward the complete picture, and everything else must sit our examination.

The arrival of AI strips that position of its default plausibility. The old picture was “human → truth.” It now has to be rewritten:

$$
\text{Human}\subset W,\qquad \text{AI}\subset W.
$$

Both are finite inquiry processes inside the world, and both travel the same path: $$W\to E\to R\to\text{action}$$. The world supplies evidence $$E$$ through an interface; evidence is organized into a representation $$R$$; action is taken on the representation and returns to the world to meet its consequences. The two differ in four places: the form of the representation $$R$$, the budget $$B$$, the questions $$Q$$ asked, and the revision rule $$\Gamma$$.

![A large field labelled W contains a human inquirer and an AI inquirer. Each obtains evidence through a finite interface, forms its own representation, acts back into the world, and both submit to shared checks. Neither stands outside W.](/assets/img/articles/aei-v5-embedded-inquirers.webp){: width="1600" height="1000" }
_Figure 1. The overview for the whole essay. No inquirer looks at the world from outside; the two kinds differ only in representation, budget, questions, and revision rule. An exact structural diagram._

One error in the opposite direction has to be blocked first. “Humans are part of the world” does not by itself prove “humans cannot describe the world completely.” In a world with a single bit, an inquirer inside it could perfectly well retain everything needed to answer every relevant question. Proving an information limit requires assumptions about capacity and questions; proving a computational limit requires assumptions about the problem. What AI takes away is the presumed status of humans as special knowers. Truth stays where it was, as a constraint.

<span id="s3"></span>

## Two layers of axioms
{: #axioms }

The first benefit of axiomatization is a place to disagree. An opponent can say which axiom does not apply, which definition is unhelpful, which inference is invalid. The axioms below come in two layers. The first describes what kind of knower we admit; the second says what counts as a fair assessment of an inquiry.

**Foundational axiom F1, embedding:** $$O\subset W$$. The knower, its tools, its records, and its acts of observation are inside the world. There is no vantage point outside it.

**Foundational axiom F2, interface and representation:** $$W\to E\to R$$. The knower obtains evidence only through a finite interface and organizes it into an internal or external working representation; claims and actions are made from that representation.

**Foundational axiom F3, finitude:** $$B_O<\infty$$. Every concrete stage of inquiry has finite memory, time, and action budgets.

From these three the reasonable form of the goal of knowing can be written down. $$R=W$$ is not excluded by logic. Under F1 to F3, however, a knower cannot obtain from the inside a certificate that $$R=W$$ has been reached; what can be checked is only conformity relative to conditions $$\mathcal C$$. The goal that can be pursued and tested is therefore $$R\approx_{\mathcal C}W$$ rather than $$R=W$$:

$$
R\approx_{\mathcal C}W.
$$

The second layer consists of operational axioms. First specify the object of an assessment: the admitted situations $$X$$, the questions $$Q$$, the record $$r(x)$$ the system receives, and the available budget. Then hold three conditions fixed.

**Operational axiom A1, fixed criterion:** within an assessment, the criterion does not change with the answer being assessed. Algorithmic correctness calls for checking inputs, outputs, and proofs; explanatory ability calls for identifying the important steps and why they matter. Adding a requirement only after discovering that the author is AI changes the test. Substituting a speed result for correctness changes it too. New criteria may be proposed, but they should be labelled as new assessments.

**Operational axiom A2, available materials:** answers depend only on materials and computations actually available to the system. Model parameters, context, tools, documents, and information from collaborators all count. An unread file cannot be treated as already known. More deliberation cannot be assumed to recover evidence that has been discarded.

**Operational axiom A3, cost accounting:** the cost of obtaining and using materials is recorded. Search, deduction, formalization, proof checking, and expert review consume different resources and are charged separately. A comparison is distorted if one system receives for free a proof the other must discover.

F1 to F3 say what a knower is; A1 to A3 say what a fair test of a claim about it looks like. These six define neither consciousness nor general intelligence. In what follows, $$x$$ denotes the actual situation, $$r(x)$$ the record available to the system, and $$q(x)$$ the correct answer to a question.

<span id="s4"></span><span id="s6"></span><span id="s7"></span><span id="s9"></span>

## First consequence: retaining an answer can erase the ability to follow it up
{: #distinctions }

Put the relevant questions together. Treat two situations as equivalent, written $$x\sim_Q x'$$, when they give the same answer to every question in $$Q$$. This does not make them the same world; it means the present task need not distinguish them.

**Proposition 1. A record is sufficient for exact answers to a set of questions if and only if all situations producing the same record give the same answers to those questions.** For every relevant question $$q$$,

$$
r(x)=r(y)\ \Longrightarrow\ q(x)=q(y).
$$

Necessity is short: identical records give the system identical material, so different correct answers cannot both be guaranteed. Sufficiency is easy too: if every situation sharing a record gives the same answers, an answer table can be filled in for that record. This establishes informational determination, not an affordable algorithm.

The minimum number of record states is therefore the number of classes into which $$\sim_Q$$ divides $$X$$. With $$m$$ classes, a fixed-length binary encoding needs at least $$\lceil\log_2 m\rceil$$ bits. This counts the record alone, not the decoder or the running time.

![The same four situations are grouped differently when asked for a, for b, or for both: the tasks require two, two, and four distinguishable record states respectively.](/assets/img/articles/aei-v2-query-partitions.webp){: width="1600" height="1050" }
_Figure 2. Questions determine the distinctions that must survive. An exact classification in a finite example, not an estimate of human memory capacity._

This gives “concept” a minimal operational model. A concept treats certain differences as irrelevant to the present questions: $$r(x_1)=r(x_2)$$ means two different microstates have been pressed into one class. The nature of a concept can be written as purpose-relative preservation of distinctions. A concept may omit details, but it cannot omit a distinction required by the questions it claims to answer. “Mean” is a good concept; using it to decide whether a distribution leaves someone behind exceeds its capacity.

A further result follows: **adding questions can make a previously sufficient summary insufficient.** If the question set grows from $$Q$$ to $$Q'$$ with $$Q\subseteq Q'$$, the distinctions required can only increase or stay the same. A concept sometimes fails because the question has changed while the record has not. Retaining an algorithm's exponent answers “What is the bound?”; a later question about which step imposes an input restriction requires the derivation that was left out.

Understanding therefore need not fall along a single scale. A system retaining only $$a$$ and one retaining only $$b$$ each store one bit; the first is better when asked for $$a$$, the second when asked for $$b$$. A score that ranks them must assign weights to the questions, and when the weights change, the ranking may change.[^blackwell]

<span id="s18"></span>

## Second consequence: repeated self-checking cannot recover evidence that is not there
{: #diagnosis }

Two obstacles need separating. The first is information that is available but not yet processed: a full proof may be on the table while checking one step needs more deduction or a formalization run; additional computation can produce a new answer without any new external observation. The second is a distinction absent from the record: if two research records retain only the same “checked” label, one of them in fact refers to the wrong version, and the system cannot reach the version and execution logs, then repeating the label will never reveal the difference.

**Proposition 2. A perfect error detector using only the current record exists only if that record uniquely determines whether the answer is erroneous.** This applies Proposition 1 to the question “Is this answer wrong?” It does not forbid risk estimates, nor sending every doubtful case for review. It rules out guaranteed case-by-case diagnosis where the distinguishing evidence is missing. Letting ten systems that hold the same record discuss the matter changes nothing; the difference lies in accessible evidence, not in headcount.

Whether “think again” helps therefore depends on the obstacle. A missed inference may yield to more computation. A missing version needs a version check. A theorem translated into a weaker formal statement needs the two statements compared. A Lean check provides evidence that a formal statement follows within a specified formal system and its dependencies; whether the prose describes that statement accurately, and whether its assumptions fit the intended problem, remain separately examinable.

Explicit probability and cost assumptions also make the verification requirement calculable. Suppose each case carries a 10% probability of an error invisible in its current summary; selection for checking is independent of actual error; unchecked cases keep their original answers; and a perfect check removes the error in every checked case. With a checked fraction $$\rho$$, the expected remaining error rate is

$$
0.1(1-\rho).
$$

Reducing it to 1% requires checking at least 90% of cases. The 10% and 1% are assumptions of this example, not measured error rates for OpenAI manuscripts or for Claude. The calculation exposes a cost that is easy to skip: producing many candidate answers does not by itself supply the capacity to raise each of them to the required reliability.

<span id="s8"></span><span id="s10"></span>

## The last way out: just find the final law?
{: #laws }

One escape route may still seem open at this point. “Fine, we need not fit every state of the world into our heads. We only need to find the universe's simple true rule; everything else can be derived.” The route looks as if it bypasses every difficulty of representation and observation.

Imagine a world of black and white cells. Each cell's next color depends only on itself and its two neighbors; three bits admit just eight combinations, so the whole rule fits on one line. Rule 110 is such a rule. Matthew Cook proved that Rule 110 supports universal computation under suitably encoded initial configurations.[^cook] A procedure that always halted and decided whether the computation encoded in any such configuration would halt could therefore solve the general halting problem, and no such procedure exists.

![The eight local update cases of Rule 110 and a finite sequence of black-and-white cells generated from a specified seed.](/assets/img/articles/aei-rule110.webp){: width="1600" height="1000" }
_Figure 3. The full local rule above a finite illustrative evolution. The image is not a proof of universality; the undecidability result relies on an unbounded family of configurations, and the depicted seed is not Cook's full encoding._

Two qualifications stay in place. The undecidability result uses an unbounded family of configurations and does not follow from the fixed finite model used earlier; questions about a specified finite region and finite time can be settled in finitely many steps, and this very image can be computed directly. Nor does the result show that the physical universe is such a system. The counterexample is enough: a short rule does not guarantee a feasible answer to every general question posed about it.

> **Simple law ⇏ cheap extraction of consequences.**

This closes the last way out. “Finding the final equation” splits into at least two achievements: knowing how the world updates, and being able to answer the questions we ask of it. The first does not automatically deliver the second. Even a wonderfully compact theory of everything would leave standing the questions of whether initial conditions are available, whether a question is decidable, and whether an answer is computable within the budget.

The same boundary shows which kind of result the Claude algorithm is. For a fully specified 3SUM input the answer is not hidden in some unpublished record; the obstacle is computational cost, and a new method changes what is feasible without adding input information. **Proposition 3. If the set of available methods expands while old methods remain available and the criterion and budget stay fixed, the set of solvable questions cannot shrink.** This does not make every new method faster. Informational sufficiency and resource sufficiency need separate assessments; calling something currently unaffordable “unknowable in principle” mistakes room for algorithmic improvement for a final limit of cognition.

A recent biomolecular-modeling project shows the other side of the boundary. In September 2026 Anthropic reported roughly fourfold overall speedups when very small numerical differences were permitted and nearly twofold speedups with identical outputs.[^bio] The same report describes runs of 31,000 to more than 70,000 tokens on a single eight-GPU B300 node whose outputs were incorrect or collapsed. Completing a very large structure prediction did not establish a correct one. An evaluation of a new method should keep at least two columns: how cost changed, and how answer quality changed.

<span id="s2"></span>

## 722 manuscripts, and three withdrawn the next day
{: #ledger }

On October 6, 2026, OpenAI released mathematical work from an internal model together with some Lean proofs and information about the research process.[^release] The initial catalogue listed 722 manuscripts across 372 result families. A manuscript count is not a count of fully confirmed new theorems.[^catalogue]

The October 7 revision log records a concrete failure. A sign error in *Algebraicity of Weil classes on split abelian eightfolds* invalidated an argument and a construction used by two dependent manuscripts. All three were withdrawn. The current catalogue lists 719 manuscripts, with 300 top-line results formalized, about 42%. These are the versioned figures as consulted on October 8.[^history]

![Versioned OpenAI manuscript counts: 722 initially, 719 after three withdrawals, with 300 top-line results formalized.](/assets/img/articles/aei-v4-release-status.webp){: width="1200" height="1060" }
_Figure 4. From the public catalogue and the October 7, 2026 revision log. Formalization status does not establish novelty or explanatory quality; lack of formalization does not establish an error._

The initial count shows the scale of production; the withdrawals and revisions show how that production becomes material for further research. When a step in an argument fails, what is lost first is the standing of the proofs that rely on it. The affected conclusions may still be true, and another proof may later establish them. Declaring them false at once goes beyond the evidence, as does continuing to treat the failed proofs as valid.

The three withdrawals were not three unrelated error labels. The revision log says that one defective argument affected a construction used by other manuscripts. Treat a conclusion as a node and attach the premises and lemmas it uses. **Proposition 4. When a necessary supporting premise loses its accepted status, every proof that currently rests on it alone loses its justification; a conclusion with an independent valid proof keeps its support.** The dependency graph marks the region that needs review. A system that keeps no dependency records will struggle to identify which answers must change. This is F2 at work: what the representation retains decides what can still be done after the evidence changes.

<span id="s11"></span>

## Fifth consequence: once a norm is chosen, it demands information
{: #norms }

Mathematical correctness is one criterion. Whether a manuscript may be labelled “verified” also depends on publication rules. On September 29, 2026, the Advisory Group on Mathematics and Artificial Intelligence, AGMAI, published recommendations asking that AI-generated mathematics state its formalization status, provenance, and citations clearly, and support human understanding of the results. These are norms proposed by a scholarly community, not ethical theorems derived from model performance.[^agmai]

Neither F1 to F3 nor A1 to A3 selects a value ordering for us. Once a norm has been chosen, however, its informational requirements can be derived. Let $$A_N(x)$$ be the actions a norm permits in situation $$x$$. A system seeing only record $$z$$ can choose an action guaranteed to comply in every possible situation only if

$$
\bigcap_{x:r(x)=z} A_N(x)\ne\varnothing.
$$

**Proposition 5. If the situations sharing a record have no commonly permitted action, the system must first obtain distinguishing information, or change its available actions or the norm.** A rule that allows “pending verification” may supply a common permitted action without immediate access to every detail; the impossibility arises only when an immediate affirmative judgment is also required.

The result adds a design check to normative discussion: a system held responsible for a distinction needs a chance to observe it. Adding a fairness score to a finished model's outputs sometimes comes too late, because the distinctions needed to assess a harm may already have vanished from the fields. For [a morality we can revise](/en/posts/a-morality-we-can-revise/) this creates a further difficulty: agreement on a better norm tomorrow does not guarantee that yesterday's decisions can be reassessed, since the evidence they would need may no longer exist.

<span id="s5"></span><span id="s12"></span>

## Sixth consequence: preserving evidence preserves the questions one can still ask
{: #future }

OpenAI's revision records retain withdrawal notices and routes to older manuscripts.[^history] A reader who only wants today's count may not need them; a researcher who later wants to know which step changed may find no substitute. The value of a record cannot be measured by today's answer rate alone.

Shrink the issue to an explicit decision model. A detail is not needed today and will be asked about later with probability $$\lambda$$. Preserving it now costs $$s$$; if it is not preserved, a reliable source can supply it later at cost $$c$$. Assume retrieval answers correctly and delay causes no extra loss. The expected costs of the two policies are

$$
C_{\mathrm{save}}=s,\qquad C_{\mathrm{retrieve}}=\lambda c.
$$

**Proposition 6. Among these two policies and under these assumptions, preserving now is cheaper if and only if** $$s<\lambda c$$. This is a conditional result, not a prescription to keep all raw data forever. If the reliable source may disappear, retrieval is no longer equivalent to preservation and a loss for unavailable answers must be added; if retention touches personal privacy, preservation itself may be prohibited.

The philosophical proposal that follows is to include revisability in the assessment of understanding. Two systems may give the same answer today while only one retains traceable grounds; a withdrawal or a new question will expose a large difference between them. Today's answer sheet does not describe the whole of a system's cognitive capacity. Part of that capacity lives in the steps it can actually take the next time something has to change.

## One set of axioms, four domains
{: #domains }

Most of the consequences above sit near research records and verification workflows. To see the reach of the axioms, run the same family of inequalities through four fields that are usually discussed apart.

**Philosophy of science.** On the night of September 23, 1846, Johann Galle at the Berlin observatory received a letter from Urbain Le Verrier in Paris containing a position computed from the irregularities in the orbit of Uranus. That same night he found Neptune within a degree of the predicted place.[^neptune] At that moment Newtonian mechanics looked like the world itself. Thirteen years later the same Le Verrier reported that Mercury's perihelion advances by about 43 arcseconds per century more than the known planets could explain; for decades people searched for a hypothetical planet, Vulcan, and never found it. On November 18, 1915, Albert Einstein read to the Prussian Academy a paper in which general relativity yielded exactly that figure of 43 arcseconds.[^mercury] Newtonian mechanics did not thereby become false; within the regime that contains Neptune it remains an excellent representation. It was always $$R\approx_{\mathcal C}W$$ with $$\mathcal C$$ excluding strong gravitational fields. It was never $$W$$ itself.

**Concept formation.** $$r(x_1)=r(x_2)$$ means two different microstates have been pressed into one class by a concept. The nature of a concept is purpose-relative preservation of distinctions, and a conceptual revolution sometimes occurs when a language has treated as identical what a new question requires to differ. Proposition 1 supplies the test: which question's answer did this merger delete?

**AI and machine learning.** $$\widehat f\approx_{\mathcal C}f^*$$, with no requirement that $$\widehat f=f^*$$. A model can perform well under a specified distribution and scoring rule without identifying the whole mechanism that generated the data. A new algorithm moves the resource boundary, not the information boundary, and the two are charged to different accounts.

**Ethics.** If a norm $$N$$ requires two situations to be treated differently while the representation merges them, $$r(x_1)=r(x_2)$$ with $$A_N(x_1)\cap A_N(x_2)=\varnothing$$, then compliance can no longer be guaranteed at the level of information. Ethics therefore reaches upstream into data design; some injustice does not come from a final decision rule computing wrongly but from an earlier step in which the system pressed into one class the people the norm required it to keep apart.

The four fields use the same axioms and the same proposition. Which distinctions a representation preserves decides which questions it can answer, which norms it can obey, and in which regime it can count as a good theory. This is where the axioms and their consequences are welded together.

<span id="s13"></span><span id="s15"></span>

## Philosophy becomes meta-inquiry
{: #philosophy }

By this point, “philosophy should study understanding” has acquired a different content.

What a ledger deletes, what a model can read, which counterexamples a test admits, and who may object to an institution are usually treated as conditions fixed before the real work begins. The consequences above show that success or failure can be settled at that earlier stage. What philosophy can do is take those conditions as its work: which questions are posed, which concepts adopted, which distinctions preserved, by which rules inference proceeds, how claims are checked, and how people may revise all of these choices. They can be analyzed separately; in the end they have to fit together in one process of inquiry that can actually run.

The direction has predecessors. In the first chapter of *Logical Foundations of Probability* (1950), Rudolf Carnap introduced explication: replacing a vague everyday concept with a more precise one that can serve in a theory, and listing the requirements by which such a replacement is judged successful.[^carnap] In “The Fixation of Belief” (1877), Charles S. Peirce compared four ways of settling belief, tenacity, authority, a priori preference, and the method of science, and argued that only a belief constrained by something outside the believer's will allows inquiry to correct itself.[^peirce] Neither “understanding depends on context” nor “philosophy can design concepts” is a discovery made here.

What this essay tries to add is a connected set of checks that applies to humans and AI alike. The range of a concept depends on the distinctions it preserves. A promise to revise depends on whether failure can become visible. Whether a norm can be followed depends on whether the merged situations still share a permitted action. Future capacity depends on executable procedures for retrieval and recoding. Most of the mathematical results have established relatives; applying them together within one philosophical proposal earns its keep only if it reveals conflicts we would otherwise have missed.

This essay calls the direction Axiomatic Embedded Inquiry, or AEI. The name refers to a revisable research program, not to a completed unified theory. It also contains one choice that no theorem can supply: to place the public assessment of understanding on warranted abilities, their scope, and practicable revision. The theorems above show which limits that usage must then face; they do not prove that everyone must adopt it.

Someone may say that an answer table could pass the earlier tasks and still understand nothing, and they would be pointing to a real gap. Informational sufficiency only answers whether a correct answer can be recovered. We may further require a system to track consequences under changed conditions, to separate causes from correlations, to reconstruct reasons, or to handle unmemorized cases at reasonable cost; each of those requirements needs its own assessment. Experience and consciousness lie outside this finite model, and neither their presence nor their absence follows from it.

<span id="s14"></span>

## Give the proposal a chance to fail
{: #experiments }

These ideas can be tested. The following designs can be planned from public materials; this essay has not run them.

**First, remove different materials and measure which capability disappears.** Prepare versions of the same questions with only conclusions, with full papers, and with papers plus dependency and revision records. Hold the model and budget fixed and separately test status recognition, explanation of assumptions, error location, and changed conditions. Where an answer is still correct, check whether it already sat in the model's prior knowledge; newly constructed controlled tasks may be needed.

**Second, let the evidence actually change.** Supply a set of verified conclusions with explicit dependencies, then withdraw one lemma. Penalize both keeping proofs whose only support has failed and indiscriminately withdrawing conclusions that have independent proofs.

**Third, compare research processes at equal cost.** One process concentrates its resources on generating candidates; another reserves a fixed share for checking, explanation, and version maintenance. Compare the number of results usable for further research, and charge external tools and human work to the budget.

![Four separately assessed tasks in one research process: generate a candidate, check the statement, explain the important steps, and handle changed conditions.](/assets/img/articles/aei-v4-evidence-tasks.webp){: width="1200" height="1380" }
_Figure 5. Each capability has its own materials and tests. Arrows mean that later work can use earlier outputs, not that passing one stage guarantees passing the next._

The three experiments will not decide whether AI is conscious. They answer more specific questions: which ways of keeping records support which abilities, which errors need new evidence rather than more computation, and which research processes leave results that others can still rely on after a challenge. The figures and numbers in this essay come from finite examples with stated assumptions and are not experimental scores of any existing system.

<span id="s16"></span>

## Put the name back
{: #return }

Now put the authors' names back on the algorithms paper. Names still matter: we ask where the data came from, who is responsible for the result, and how to allocate the effort of checking. A valid proof does not lose its validity on that account, and an author who resembles us cannot vouch for an invalid inference.

The road this essay has travelled fits in one line. AI produced discoveries without possessing a true representation; machine learning shows that this kind of knowing was always approximation under stated conditions; the leap from “truth exists” to “a finite knower will possess it” therefore loses its default standing; humans and AI are both finite inquiry processes inside the world; axioms written down for that situation yield concrete conditions on concepts, verification, computation, norms, and revision; the same conditions run through science, concept formation, machine learning, and ethics; and the work of philosophy moves from painting the final picture of the world to designing and checking the conditions of inquiry itself.

Laplace placed the all-knowing intelligence forever out of human reach; Hilbert believed we shall know; Gödel, in the same city, pointed to the crack in that road. What AI changes denies none of what any of them wanted to know. It removes a position: no knower, human or machine, naturally stands outside the world looking down on truth. Truth remains, as a constraint, as the thing that makes every representation right or wrong.

Understanding can accordingly be rebuilt as a set of abilities with a scope: forming the necessary distinctions, reasoning with them, submitting claims to suitable checks, recognizing when a representation fails, and finding a way to acquire new distinctions. Different bodies, tools, and forms of cooperation can realize these abilities; they need not all resemble what human introspection finds familiar. This is the space left open by [From Reaction to Heterogeneous Rationality](/en/posts/from-reaction-to-heterogeneous-rationality/), and the retention, combination, and return of [No View Is the Whole](/en/posts/no-view-is-the-whole/) here take a form that can be written as conditions.

Thought is entitled to be corrected by a world it does not completely possess. The strength of a philosophy can be measured by how many new abilities that correction makes possible.

<span id="s17"></span>

## Sources and version note
{: #references }

Sources were checked on **October 8, 2026**. Recent results are described from original papers, institutional reports, and revision records; this essay has not independently rerun every Lean proof and does not treat a preprint or institutional report as completed external peer review. Its axioms, propositions, and experimental designs are analyses under stated conditions, without any claim of priority for the underlying mathematical observations; the experiments have not been performed.

[^algorithm]: Josh Alman and Virginia Vassilevska Williams, [*Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs*](https://arxiv.org/abs/2610.06783), arXiv:2610.06783v1, October 5, 2026. The bounds are those of the abstract, in its stated integer regimes; they are not measured practical runtimes.
[^method]: The paper's [Acknowledgments and Methodology](https://arxiv.org/html/2610.06783v1) describes the discovery, the human contributions, and the subsequent Lean certification, with a link to [anthropics/formal-math — 3sum-apsp](https://github.com/anthropics/formal-math/tree/main/3sum-apsp). The account here does not describe the project as human-free.
[^uml]: Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014). [Authors' textbook](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf). The equations show one basic supervised-learning setting, not every form of learning.
[^laplace]: Pierre-Simon Laplace, *Essai philosophique sur les probabilités* (1814); English translation *A Philosophical Essay on Probabilities*, trans. F. W. Truscott and F. L. Emory (1902), opening of Chapter II. [Full text at Project Gutenberg](https://www.gutenberg.org/ebooks/58881). The “feeble idea” and “infinitely removed” sentences immediately follow the famous passage.
[^hilbert]: For the dates of the conference and Gödel's remark see the [Stanford Encyclopedia of Philosophy, “Kurt Gödel”](https://plato.stanford.edu/entries/goedel/); for Hilbert's address of September 8, 1930 in Königsberg, “Naturerkennen und Logik,” and its radio recording, see the [nLab entry](https://ncatlab.org/nlab/show/Naturerkennen+und+Logik), which cites the original and the English translation.
[^blackwell]: David Blackwell, “Equivalent Comparisons of Experiments,” *Annals of Mathematical Statistics* 24(2), 265–272 (1953). [DOI](https://doi.org/10.1214/aoms/1177729032). The value of information across decision problems has an established theory; the one-bit example is an elementary construction.
[^cook]: Matthew Cook, “Universality in Elementary Cellular Automata,” *Complex Systems* 15(1), 1–40 (2004). [Original paper page](https://www.complex-systems.com/abstracts/v15_i01_a01/). Universality requires suitable configurations; a finite single-seed image does not establish undecidability or a general absence of shortcuts.
[^bio]: Anthropic, [How Claude is uplifting biomolecular modeling](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling), September 17, 2026. Publisher-reported results; identical outputs and permitted numerical differences are different evaluation conditions. The very large runs used one eight-GPU B300 node.
[^release]: OpenAI, [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/), October 6, 2026.
[^catalogue]: OpenAI, [math repository](https://github.com/openai/math) and [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md). The initial 722 manuscripts and 372 families must be read alongside the current 719-manuscript count and the withdrawal record.
[^history]: OpenAI, [history.md](https://github.com/openai/math/blob/main/history.md), October 7, 2026 revision entry. Source for the withdrawals, other revisions, retained older versions, and the 300/719 formalization figure.
[^agmai]: Advisory Group on Mathematics and Artificial Intelligence, [Responsible Release of AI-Generated Mathematics](https://agmai.org/general-sep29/), September 29, 2026. These recommendations do not certify individual results.
[^neptune]: For the discovery see [Wikipedia, “Discovery of Neptune”](https://en.wikipedia.org/wiki/Discovery_of_Neptune): Galle observed Neptune on the night of September 23, 1846, within a degree of Le Verrier's predicted position.
[^mercury]: Albert Einstein, “Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie,” *Sitzungsberichte der Preussischen Akademie der Wissenschaften* (1915), 831–839, read on November 18, 1915. The anomalous advance of about 43 arcseconds per century was reported by Le Verrier in 1859; for background see [Wikipedia, “Tests of general relativity”](https://en.wikipedia.org/wiki/Tests_of_general_relativity).
[^carnap]: Rudolf Carnap, *Logical Foundations of Probability* (1950), Chapter I, §§2–3, on the task and requirements of explication. [Scan](https://www.fitelson.org/confirmation/carnap_logical_foundations_of_probability.pdf).
[^peirce]: Charles S. Peirce, “The Fixation of Belief,” *Popular Science Monthly* 12, 1–15 (1877). [Transcription](https://www.peirce.org/writings/p107.html).
