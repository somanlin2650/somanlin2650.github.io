---
layout: post
title: "AI Forces Us to Ask Again What Understanding Means: Axioms of Finite Cognition and the Reconstruction of Philosophy"
date: 2026-10-08 11:30:00 +0800
last_modified_at: 2026-10-08 12:43:35 +0800
lang: en
permalink: /en/posts/understanding-without-possessing-the-world/
alternate_url: /posts/understanding-without-possessing-the-world/
categories: [AI, Philosophy]
tags: [Artificial Intelligence, Epistemology, Axiomatic Philosophy, Understanding, Representation, Revisability, No View Is the Whole]
description: "If finite AI representations can support checkable reasoning, must understanding require possession of complete truth? Six core axioms and three inquiry rules yield consequences for concepts, abstraction, blind spots, macro-level laws, ethics, and revisable intelligence."
toc: true
comments: true
math: true
---

Suppose an AI could expose a contradiction in our most trusted philosophical argument, introduce a more precise concept, and resolve a problem we had struggled with for years. Its achievements would not rest on persuasion alone: proofs could be checked, predictions tested, and counterexamples reproduced.

We would know how it was built. It learned from finite data, operates within finite resources, uses its own representations, and revises answers through reasoning and tools. It has neither copied the entire world into a machine nor acquired an infallible claim to omniscience.

If we nevertheless insisted that it did not truly understand, we would owe an answer: **What exactly is missing—and when did human beings acquire that missing qualification?**

This thought experiment does not assume that AI has already surpassed every philosopher. It brings a question about criteria into view: when publicly checkable cognitive achievement separates from a familiar internal form, which is necessary for understanding? Mathematical systems already exert a limited but concrete pressure. AlphaGeometry combines neural proposals of auxiliary constructions with symbolic deduction to produce checkable geometry proofs. This does not establish every human capability, but it makes unfamiliar reasoning an insufficient objection to the achievement.[^ag]

The philosophical impact of AI begins here: **as we manufacture another kind of knower, we must reexamine the qualifications for knowing instead of letting human self-experience settle them alone.**

This essay develops an axiomatic core for finite cognition and derives consequences for concepts, ontology, causation, ethics, and the design of intelligence. The value of axiomatization lies in what it makes derivable, contestable, and possible to design.

## 1. AI exposes something knowing already does
{: #s1 }

A learning system need not identify a unique world-generating mechanism before it can accomplish a task. In a basic supervised-learning setting, it selects a model $$f$$ to reduce risk under a data distribution $$D$$ and loss function $$\ell$$:

$$
R_D(f)=\mathbb E_{(x,y)\sim D}[\ell(f(x),y)].
$$

Training generally does not provide direct access to this expectation. It uses finite data and empirical risk, while independent testing, theoretical assumptions, and later observations inform judgments about generalization.[^uml] A model can make sufficiently reliable predictions within a specified scope without being the uniquely correct generative model. Some learning problems do seek identification of true parameters or functions. The relevant point is that **successful performance does not universally require global identification**.

Writing $$f^*$$ for an ideal target in a specified setting, we can abbreviate the relationship as

$$
\widehat f\approx_{\mathcal C}f^*.
$$

The context subscript matters: which situations, questions, tolerances, and resource limits? Low average loss does not imply correctness at every input. With noise, optimal prediction need not be a deterministic “true world function.”

![Two constructed functions coincide throughout a specified task interval and diverge outside it, showing that local agreement does not imply global identity.](/assets/img/articles/aei-v2-task-fit.webp){: width="1600" height="900" }
_The illustrative functions deliberately coincide within the interval. This is a counterexample to inferring global identity from local agreement, not experimental data or a claim that finite testing proves agreement throughout an interval._

The philosophical question is whether this finite, approximate, testable mechanism should remain an engineering expedient or become a general model of finite cognition as it supports more activities we call understanding.

A high AI score does not establish the entire nature of the human mind. It does, however, relocate the burden of proof. If complete possession of an object is proposed as a necessary condition of understanding, we need to know how that condition is assessed, why it is necessary, and what warrants believing that humans satisfy it.

A more useful relationship between world and representation is preservation of usable structure for explicit questions. The notation $$R\approx_{\mathcal C}W$$ abbreviates requirements that must be unpacked into errors, evidence, and operational conditions. It does not posit an undefined universal distance between a representation and the cosmos.

## 2. Truth's existence grants nobody automatic possession of it
{: #s2 }

“The world has a real structure” and “finite reason will eventually possess that structure completely” are different propositions. The first does not logically guarantee the second.

Epistemic arrogance can reside in this unaccounted-for step. It need not claim omniscience today. It can assume that all successful inquiry must ultimately converge on one complete, unique world-picture whose consequences are fully available to its knower.

AI makes another possibility concrete: a system could be more capable than us on important questions without depending on that possession. If so, complete possession of truth cannot simply be installed as cognition's highest endpoint without argument.

This does not reduce human achievement to illusion. Acquiring knowledge that survives examination and treating the feeling of intellectual closure as a certificate of completeness are different acts. The former can succeed while the latter fails.

Philosophy can accordingly shift part of its attention from acquiring a final world-picture to an equally fundamental question: **Which concepts, distinctions, inferences, and revision mechanisms allow knowers inside the world to keep acquiring reliable knowledge?**

## 3. State the axioms: what kind of knower is being modeled?
{: #s3 }

Call this core *Axiomatic Embedded Inquiry*, or AEI. It axiomatizes conditions of knowing before stipulating the ultimate substance of the universe. Different ontologies and ethical systems can then state their assumptions within a shared framework of accountability.

Let $$X$$ denote the possible situations considered in an inquiry; $$H$$ an observational interface; $$E$$ available evidence; $$r$$ a way of organizing evidence into an internal or external working representation; $$Z$$ the possible representations; $$Q$$ a set of questions; and $$B$$ a resource budget. Where dynamics matter, specify a transition $$F$$. This does not assume that every world must be deterministic.

The following six axioms define the core model. They are explicit starting conditions, not conclusions smuggled into rhetoric.

| ID | Axiom | Shortcut excluded |
| --- | --- | --- |
| A1 | **External constraint:** the satisfaction conditions of empirical claims are not arbitrarily determined by the knower's current assent | Believing something makes it true |
| A2 | **Embedded accounting:** knowers, tools, external memory, and observations belong to the environment, with their costs charged to a shared budget | Treating tools or queries as free omniscience |
| A3 | **Mediated access:** an answer depends only on accessible evidence, prior state, and permitted operations | Using a distinction never obtained |
| A4 | **Local finitude:** each concrete inquiry stage has finite memory, time, and action budgets | Invoking infinite computation to certify a present capability |
| A5 | **Question indexing:** sufficiency and error are evaluated relative to explicit questions, situations, and costs | Turning success on one task class into success on every question |
| A6 | **Traceable warrant:** a supported claim in this system retains its dependencies on assumptions, evidence, inference, and verification scope | Preserving a conclusion while inheriting unexplained authority |

A1–A5 constrain the modeled agent and its evaluation; A6 specifies what counts here as inspectable warrant. It does not assert that every real person maintains such records. Embedded agency already has an established research literature; this essay places part of that problem setting within a framework of explicit derivation.[^embedded]

Write an inquiry context as $$\mathcal C=(X,Q,D,\ell,B,V)$$, where $$D$$ is a distribution when appropriate and $$V$$ a verification procedure. Scenario sets or worst-case analysis can replace an unjustified probability model. Normative premises belong in a separate module $$N$$ rather than hiding inside descriptive notation.

Add three **rules of inquiry**, distinguished from informational limitations:

1. **Retractability:** reassess a claim when a condition supporting its warrant is defeated. AEI itself is included.
2. **Layered revision:** record changes to answers, representations, observations, and evaluation standards as different operations. A hidden change of standard is not demonstrated improvement.
3. **Normative bridging:** substantive conclusions about what ought to be done must expose their normative premises and connecting reasons. A descriptive model does not independently select an arbitrary value ordering.

These are requirements adopted for accountable inquiry, not facts mechanically deduced from a memory limit. Axiomatization first provides a place to disagree: an axiom may be inapplicable, a definition unhelpful, an inference invalid, or a rule objectionable. The following results show what these commitments enable.

## 4. Consequence one: the minimal unit of knowledge is a required distinction
{: #s4 }

Begin with a finite deterministic situation set and a finite question family. Combine observation and representation into $$r:X\to Z$$ for the proof. This shorthand does not grant an agent direct access to $$x$$.

Define two situations as equivalent exactly when every relevant question has the same answer in both:

$$
x\sim_Qx'\quad\Longleftrightarrow\quad\forall q\in Q,\ q(x)=q(x').
$$

This partitions situations into groups that the present questions do not require us to distinguish. **P1: a representation is informationally sufficient for exact answers to all of $$Q$$ if and only if it never merges situations belonging to different task-equivalence classes.**

For necessity, identical representations give an answering procedure identical input, so every question must have a constant answer within each representation class. For sufficiency, assign each class its common answer for each question. This constructs a decoder. It establishes informational existence, not affordable execution.

If there are $$m$$ task-equivalence classes, at least $$m$$ representation states are required, or $$\lceil\log_2m\rceil$$ bits in a fixed-length code. This counts state encoding, not the description costs of the decoder or questions.

![The four binary situations 00, 01, 10, and 11 form different partitions when the questions concern the first bit, the second bit, or both.](/assets/img/articles/aei-v2-query-partitions.webp){: width="1600" height="1050" }
_The world stays fixed while the required representation changes. For the first-bit question, 00 and 01 can be merged. Answering both bits requires all four states to remain distinct._

This supplies a minimal operational model of a concept: it treats certain differences as irrelevant to present questions. It is not a complete definition of linguistic meaning, but gives conceptual engineering a checkable task: what exactly has this grouping removed?

The philosophical consequence is immediate. **The minimum information required for knowing is not determined by the object's size alone, but by what must be distinguished.** An enormously complex object may require one bit for one question; a four-state system may resist further compression for another question family.

Successful abstraction preserves necessary distinctions rather than creating a miniature copy of the world. The information bottleneck and comparison of statistical experiments study related trade-offs from different directions. The elementary factorization here is not claimed as a new mathematical discovery.[^ib][^blackwell]

## 5. Consequence two: a perfect abstraction today may have no room to grow
{: #s5 }

Expand the question set from $$Q$$ to $$Q'$$. If a new question distinguishes formerly equivalent situations, their class must split.

**P2: once a representation has merged a distinction required by a new question, no procedure operating only on that representation can guarantee recovery of the answer.** This follows directly from P1. A redundant question may require no extra information; what matters is whether it introduces a necessary distinction.

A stronger result follows. Every lossy representation admits some new binary question it cannot answer exactly: choose merged states $$x_1,x_2$$ and assign them different answers.

Thus **genuine information loss cannot coexist with guaranteed sufficiency for every arbitrary future question without acquiring additional information**. A known, restricted question family may still permit substantial compression.

This changes how learning should be evaluated. Perfect scores on fixed questions may show only that the system found a sufficient grouping for those questions. When a future task requires another distinction, more training of the same kind may be less useful than dismantling a classification responsible for earlier success.

Education, science, and organizations all encounter this problem. A report retaining only averages can answer aggregate questions accurately while failing on distribution. Records organized around old products may not answer questions about new uses. The old system need not have been wrong before, but its previous correctness does not grant an automatic extension of scope.

**A conceptual revolution may occur when a language has treated as identical what a new question requires to differ.**

## 6. Consequence three: some errors have an irreducible floor
{: #s6 }

Allowing errors gives a quantitative version of the boundary.

For finite situations, deterministic target answers, known distribution $$D$$, and 0–1 loss, the best error attainable from representation $$r$$ alone is

$$
L^*(r;q)=1-\sum_z\max_y P_D(r(X)=z,\ q(X)=y).
$$

**P3: this is a lower bound for every answering procedure using only $$r$$.** Within each representation class, the best answer is the most probable one. Summing those probabilities gives maximum accuracy; the remainder is unavoidable error. More elaborate post-processing cannot separate target answers hidden inside the same class.

Return to four equally probable situations $$X=(a,b)\in\{0,1\}^2$$. Retain only $$a$$, but ask for $$b$$. Each representation class contains equal numbers of 0 and 1 answers, so maximum accuracy is 50%. More reasoning does not turn it into 90%. Reliably observing $$b$$ changes the informational conditions instead.

![In the hidden-bit example, extra reasoning leaves minimum error at 50 percent; obtaining the missing bit allows ideal error to fall to zero.](/assets/img/articles/aei-v2-error-floor.webp){: width="1600" height="900" }
_These are analytic results for the four-state model. Extra reasoning excludes new observations. Acquiring a bit is a different operation with a cost, not a free architectural advantage._

This yields a diagnostic research priority: determine whether the bottleneck lies in available information before assuming the solver needs improvement. Once a representation imposes an irreducible floor, optimizing its decoder attacks the wrong constraint.

In real applications, $$D$$ is usually unknown, so this limit cannot simply be read from a training score. Controlled environments can establish bounds; paired counterexamples can defeat exact guarantees; experiments can then test whether additional observations or preserved distinctions help. Proof and estimation remain different activities.

## 7. Consequence four: agreement does not necessarily add evidence
{: #s7 }

Suppose a hundred Agents all receive the same representation $$r(x)$$. They converse, paraphrase, and vote, using randomness that contains no additional information about the state. Their final result is still post-processing of $$r(x)$$.

**P4: this collective cannot beat P3's informational error floor.** More members can reduce individual computational errors and improve search or calibration. They cannot restore a distinction missing from all their inputs.

Likewise, a self-checker reading only $$r(x)$$ cannot always identify whether the current answer is correct when two states share that representation but require different answers. Ten critical phrasings of the same blind spot do not become independent evidence.

An additional channel preserving the missing distinction changes the situation. If one Agent retains $$a$$ and another $$b$$, their joint representation $$(a,b)$$ supports both questions. The gain comes from complementary distinctions, not headcount alone.

Public verification consequently means more than many people examining the same material. It requires opportunities to obtain different evidence, operate different instruments, or inspect conditions the original system omitted. Objectivity can be supported by a structure of shared correction without requiring identical intuitions.

For the diagnostic problem in [When AI Cannot See Its Own Hypoxia](/en/posts/when-ai-cannot-see-its-own-hypoxia/), this is a sharper condition: an outside observer matters because it can preserve a distinction unavailable internally. It need not be another named Agent; an independent monitoring channel can suffice.

## 8. Consequence five: macro-level autonomy has a checkable condition
{: #s8 }

After mapping a detailed state $$x$$ into $$r(x)$$, can we predict at the summarized level without repeatedly recovering every detail?

For deterministic dynamics $$F:X\to X$$, seek a macro-level transition $$\overline F$$ satisfying

$$
r(F(x))=\overline F(r(x)).
$$

**P5: such a deterministic transition exists if and only if states merged now remain mapped to the same macro-state after one transition.**

Necessity follows because identical macro-input has one macro-output. For sufficiency, define each class's successor to be the common successor class of its members. This is the basic factor-map condition for dynamics.

A failing example is $$F(a,b)=(b,a)$$ with $$r(a,b)=a$$. States 00 and 01 both currently appear as 0; their next represented states are 0 and 1. Identical represented presents lead to different represented futures.

![Swapping two binary coordinates does not give a closed one-step rule when only the first coordinate is retained; retaining both coordinates does.](/assets/img/articles/aei-v2-macro-closure.webp){: width="1600" height="1050" }
_The detailed dynamics are deterministic, but the merged representation lacks a deterministic one-step update. Additional state, or suitable history under appropriate conditions, can repair the gap._

Two philosophical consequences follow. First, uncertainty at a representational level need not demonstrate uncertainty in the underlying dynamics. Omitted details may become relevant at the next step. This is a concrete counterexample, not a claim that all randomness is reducible.

Second, the legitimacy of higher-level objects can partly be investigated through stability under relevant operations. Concepts such as temperature, species, and organizations need not earn their usefulness by appearing on a fundamental particle list. They require their own definitions, scales, and approximation conditions. Higher-level causal claims additionally need compatibility with admissible interventions.

Ontology gains a practical question: **Which distinctions support a level with usable regularities, and which objects are artifacts of an unstable grouping?** Exact closure is an ideal case. Real systems may require approximate closure and error analysis; a binary example is not a theorem about every macro-science.

## 9. Consequence six: longer debate cannot distinguish observationally equivalent theories
{: #s9 }

If two candidate world models produce the same evidence distribution under every currently permitted observation and intervention, any test using those procedures receives identically distributed data.

**P6: evidence obtained through those permissions cannot reliably identify which model is present.** With equal prior probabilities over the models, optimal identification accuracy is one half. Additional assumptions or prior preferences may favor one, but their contribution should be explicit.

Causation supplies a concise example. Let $$U$$ be a fair binary variable. Model A has $$X=U,Y=X$$; model B has $$X=U,Y=U$$. Passive observation produces 00 and 11 with equal probabilities under both. Set $$X$$ externally to 0, however, and A has $$Y=0$$, whereas B's $$Y$$ still varies with $$U$$. Identical observational distributions permit different interventional answers.[^pearl]

This does not imply that every causal inference requires conducting an experiment. It means that moving from observation to intervention needs identifiable structural assumptions or additional evidential access.

Philosophical disputes can begin with the same diagnosis. Where do rival positions differ in accessible evidence, inferential commitments, or practical consequences? Ontological alternatives may remain meaningful even when presently indistinguishable, but a difference in language should not be presented as one already settled by existing data. Changing observation and intervention conditions may accomplish more than another round of the same debate.

## 10. A final law would not provide every consequence
{: #s10 }

One apparent escape remains: discover the world's simple underlying rule, and all problems of representation and observation will disappear.

A short rule need not make its consequences cheap. Rule 110 needs only eight local update cases and supports universal computation under suitable configurations. If an analyzer could always terminate and correctly determine whether the computation encoded in every corresponding initial configuration halts, it would solve the halting problem. Such a universal analyzer does not exist.[^cook]

![The eight update cases for Rule 110 and a finite simulation of 120 updates from one active cell.](/assets/img/articles/aei-rule110.webp){: width="1600" height="1000" }
_This finite image can be computed directly. Universality and undecidability concern appropriately encoded configurations and unbounded questions, not the visual complexity of this example._

**P7: knowledge of a generating rule does not generally guarantee a terminating answer to every consequence question, much less an answer within a finite budget.** This does not assume our universe satisfies the computational conditions. The counterexample already defeats the general inference from simple rules to comprehensive understanding.

A finite image generated by a short rule and simple initial condition may still have a short description. Description length and evaluation cost must remain separate. The relevant conclusion is

$$
\text{Theory of Everything}\ \not\Rightarrow\ \text{Understanding of Everything}.
$$

Even where undecidability plays no role, equal information can yield different capabilities. Store a binary string, or store all its prefix parities. The two encodings use the same number of bits and can be converted back and forth. But asking for an arbitrary prefix's parity requires inspecting that prefix in a bit-query model for the first encoding, while the precomputed encoding needs one lookup. Preprocessing costs something and may pay off through repeated queries.

Representation design therefore concerns both what is preserved and which operations become cheap. An account of cognition consisting entirely of lossy compression misses the second dimension.

## 11. Consequence seven: ethics determines what must not be forgotten
{: #s11 }

A1–A6 do not select a unique value ordering. The same descriptive facts can admit different normative additions supporting different choices. If both extensions are compatible with the descriptive premises, those premises do not independently determine that particular ought. This is a countermodel argument under consistent premises without hidden normative bridges; it does not define normative truth out of existence.

The first part of **P8** is that ethical inference must expose its normative module $$N$$. Its consistency, consequences, scope, and reasons can be examined. Successful model fitting does not settle its justification.

The second part is less obvious: once a norm is specified, it changes which information may be discarded.

Suppose an institution stores only the mean resources of two people. Group A has 40 and 60; group B has 0 and 100. Both means are 50. Under the norm “initiate support if anyone is below 20,” the groups require different responses. A system retaining only the mean cannot guarantee that distinction, however much downstream fairness checking it adds.

P1 immediately gives the consequence: **if a norm requires different treatment of two situations, representation must preserve enough information to distinguish them.** Complete personal records are not always necessary; the minimum or an appropriate threshold indicator could suffice here. Required retention still depends on the question and costs.

Ethics thus enters question formation, evidence acquisition, and summarization rather than appearing only as a final loss function. Some injustice arises before the decision rule: the system has already made people identical whom the adopted norm requires it to distinguish.

The public examination advocated in [A Morality We Can Revise](/en/posts/a-morality-we-can-revise/) consequently has informational prerequisites. Affected people must be able to identify a merged distinction, and the institution must have somewhere to receive that counterexample.

## 12. Consequence eight: revisability concerns reachable representations
{: #s12 }

Two Agents can behave identically today while differing radically in tomorrow's capacity to repair. One retains access to original evidence; the other retains only a summary. A new question allows the former to recover a distinction while the latter can only reconsider the same summary.

Let $$\mathcal R_B(O)$$ be the representations an agent $$O$$ can reach through permitted observations, memory, and updates within an additional budget $$B$$. For a future question $$q$$, consider

$$
L^{\mathrm{reach}}_B(O;q)=\inf_{r'\in\mathcal R_B(O)}L^*(r';q).
$$

This is an informational reachability bound. Finding a suitable representation and executing a decoder in time remain further requirements.

**P9: current task performance does not by itself determine future revisability.** Agents with identical summaries but different reacquisition permissions provide a counterexample. If one reachable set includes another, with the cost of maintaining options fairly accounted for, its best reachable loss cannot be worse. Its actual strategy can still choose badly.

Part of intelligence shifts from what is known now to where inquiry can go after failure. Evidence access, instruments, replaceable representational layers, and reversible updates become parts of capability rather than merely administrative surroundings.

Preserving revision options therefore has conditional future value. It costs resources and is not always worthwhile. Eliminating it based solely on present accuracy may nevertheless remove the only route to future improvement.

**P10 adds a complementary limit: if an agent can freely rewrite its evaluator and receives reward only for acceptance, an “accept everything” evaluator yields a perfect score without improving its world model.** This is a constructive degenerate solution. Revisability cannot mean unrecorded freedom to change anything. Altering an evaluation standard requires a further layer of traceable reasons and scrutiny.

That scrutiny remains finite too; it is not an infallible final judge. The practical demand is to expose dependencies and changes, retain counterexamples, and allow revised standards to encounter resistance rather than requiring infinite self-certification before inquiry can proceed.

## 13. Philosophy's second-order work: redesigning the space of questions
{: #s13 }

The relationship between philosophy and machine learning can now be stated more precisely.

Inside an established learning problem, parameters are adjusted to improve answers. Another level changes features, observation, and hypothesis spaces. A further level asks why this is the question, why a distinction matters, what counts as evidence, who bears the cost, and which norms make an answer a reason for action.

Modern machine learning already includes representation learning, active learning, model selection, and meta-learning. It should not be reduced to blind optimization inside fixed features, nor should representation change be reserved for philosophy. Philosophy's role here is the public examination and reconstruction of **the relations among questions, representations, warrant, and norms**.

![Three connected levels of inquiry: solving within a representation, revising observation and representation, and reconsidering questions and norms. Changes at the third level require explicit reasons and authorization.](/assets/img/articles/aei-v2-inquiry-levels.webp){: width="1600" height="1100" }
_These are levels of operation, not mutually exclusive disciplines or categories of intelligence. A person or AI can work across them, and higher-level revisions can fail._

Axiomatization acts like a type discipline for arguments. Formal conclusions state their axioms; empirical conclusions their observational support; normative conclusions their value premises. Moving between them requires an explicit bridge rather than a word quietly changing meaning.

“Overall model accuracy improved” is empirical. “Every affected group improved” needs additional subgroup evidence. “Therefore it should be deployed everywhere” needs normative premises about risks, rights, and responsibility. Appearing in one report does not make these the same kind of conclusion.

Explication, fallible inquiry, and information comparison all have substantial predecessors.[^carnap][^peirce] The work here is to connect them into an inspectable chain: **which worldly distinctions are preserved, which operations become possible, which evidence licenses a conclusion, and which component can change after failure.**

This joins the retention, combination, and return developed in [No View Is the Whole](/en/posts/no-view-is-the-whole/) with the heterogeneous representations discussed in [From Reaction to Heterogeneous Rationality](/en/posts/from-reaction-to-heterogeneous-rationality/). Different modes of thinking need not become identical intuitions before shared verification can connect them.

## 14. From axioms to design: three experiments that can fail
{: #s14 }

A useful framework should identify worthwhile interventions and state what results would restrict its claims.

**First, separate informational from computational bottlenecks.** In a controlled world, construct tasks lacking a necessary bit and others containing all necessary information but requiring expensive solution procedures. Under matched total costs, compare more reasoning, renewed observation, and recoding. Additional reasoning should help only some of the second class. Claims to beat a proved informational bound without new information should first trigger checks for leakage, prior correlations, or a mistaken setup.

**Second, measure the repair cost of abstraction.** Begin with identical questions, then introduce questions splitting old equivalence classes. Compare fixed summaries, accessible original evidence, and adaptive refinement under matched storage, querying, and computation costs. Measure new-task performance, repair time, regression, and mistaken updates. If revisability does not compensate for its costs, restrict its deployment conditions.

**Third, measure a team's informational complementarity, not its headcount.** Under a fixed total budget, compare Agents sharing the same summary with Agents able to obtain complementary signals. The former may improve computation through division of labor, but should not beat the relevant common-information bound. Any advantage of the latter must account for observation costs rather than crediting extra data to architectural magic.

A candidate system would maintain a question-and-warrant record, a routine solver, a representation-failure diagnostic, budgeted observation and recoding procedures, and a validator with held-out cases. Failure would be routed toward observation, representation, computation, or objective specification instead of always returning to “think again.”

Even whether to revise admits a simple criterion. If a one-time representational change costs $$c$$ and reduces expected loss by $$\Delta$$ per subsequent task, then under commensurate units, a stationary task, and equal later running costs, revision is worthwhile over $$N$$ remaining tasks when $$N\Delta>c$$. Uncertain benefits, changing tasks, and regression require additional terms. Deeper understanding can be an investment in reconstruction rather than a ritual that every task must pay for anew.

## 15. Which philosophical questions change their form?
{: #s15 }

These consequences do not settle philosophy at once, but they change the structure of several questions.

| Familiar question | Further question enabled by the framework |
| --- | --- |
| Does a concept reflect an essence? | Which situations does it merge, for which questions is it sufficient, and what new question would force it to split? |
| Are macro-level things real or merely descriptions? | Does that level support stable, approximately closed regularities compatible with relevant interventions? |
| Does agreement bring us closer to truth? | Does it combine complementary evidence or reproduce the same missing distinction? |
| Why does more thought fail? | Is the missing element evidence, a distinction, an algorithm, a budget, or an acceptable norm? |
| Which equally high-scoring system is more intelligent? | Which representations can each reach under the same budget after tasks change? |
| Can fairness be added as a final check? | Have distinctions required by the norm already been removed upstream? |
| Can introspection complete self-knowledge? | Which correctness distinctions never enter the checking channel when action and introspection share a representation? |
| Would a final law yield complete understanding? | Are initial conditions available, questions decidable, and answers computable within resources? |

Some foundations are established mathematics; some are philosophical consequences of connecting those foundations; others remain empirical design hypotheses. Their strength does not require every component to be unprecedented. It requires explicit premises to keep generating checkable consequences.

## 16. Understanding need not end in a closed copy of the world
{: #s16 }

AI's deepest challenge may be less how many unknown answers it will supply than what it reveals about the possibility of different representational routes to knowledge. Each route still faces the world, questions, resources, and error.

Understanding can consequently be reconstructed as a dynamic set of capabilities: forming necessary distinctions, using their relations to infer, submitting claims to suitable checks, detecting representational failure, and finding ways to acquire new distinctions. This is a proposed working reconstruction. Consciousness and subjective experience retain their own questions; a successful task model does not erase them.

Axiomatic philosophy need not conclude with an unrevisable set of answers. A productive form exposes premises, derives limitations, compares alternatives, and makes its own failure conditions visible. It can say both “more reasoning alone cannot solve this” and “progress requires changing this particular condition.”

**Truth constrains; questions determine necessary distinctions; computation limits usable capability; inquiry opens paths to revision.**

Human beings need not surrender the ambition to know the world. They can surrender the assumption that their desired completeness is an endpoint every form of cognition must promise. Thought can answer to a world it does not completely possess. A philosophy's power can lie in how many new capabilities that answerability makes possible.

## Notes and references
{: #s17 }

[^ag]: Trieu H. Trinh et al., “Solving olympiad geometry without human demonstrations,” *Nature* 625, 476–482 (2024). [Paper](https://www.nature.com/articles/s41586-023-06747-5). Neural proposals and symbolic deductions illustrate publicly checkable capability, not established general philosophical superiority.

[^uml]: Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014). [Authors' manuscript](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf). Population risk, empirical risk, and generalization are distinct. Finite testing is not proof of global identity.

[^embedded]: Abram Demski and Scott Garrabrant, “Embedded Agency” (2019). [Paper](https://arxiv.org/abs/1902.09469). The axioms and inquiry rules here are this essay's arrangement, not a claim to reproduce an existing complete system from that paper.

[^ib]: Naftali Tishby, Fernando C. Pereira, and William Bialek, “The Information Bottleneck Method” (1999; arXiv version 2000). [Paper](https://arxiv.org/abs/physics/0004057). Task-relevant compression is not the only route to representational improvement.

[^blackwell]: David Blackwell, “Equivalent Comparisons of Experiments,” *The Annals of Mathematical Statistics* 24(2), 265–272 (1953). [Paper](https://doi.org/10.1214/aoms/1177729032). The finite deterministic examples here do not purport to reprove the general theorem or equate informational dominance with superiority after all costs.

[^pearl]: Judea Pearl, “Causal inference in statistics: An overview,” *Statistics Surveys* 3, 96–146 (2009). [Author's paper](https://ftp.cs.ucla.edu/pub/stat_ser/SS-2009-57-Sup.pdf). Structural causal models distinguish observational distributions from intervention questions. The binary example here illustrates that distinction.

[^cook]: Matthew Cook, “Universality in Elementary Cellular Automata,” *Complex Systems* 15(1), 1–40 (2004). [Paper and download](https://www.complex-systems.com/abstracts/v15_i01_a01/). Universality requires suitable configurations; the finite single-seed image does not establish undecidability or a universal lack of shortcuts.

[^carnap]: Rudolf Carnap, *Logical Foundations of Probability* (1950), chapter 1 on explication. [Book](https://www.fitelson.org/confirmation/carnap_logical_foundations_of_probability.pdf). Conceptual reconstruction has philosophical predecessors; AI did not invent the study of concepts.

[^peirce]: Charles S. Peirce, “The Fixation of Belief” (1877). [Original text](https://www.peirce.org/writings/p107.html). Fallible inquiry has a long history. This essay organizes some of its conditions around artificial knowers that can be designed and compared.
