---
layout: post
title: "From Reaction to Heterogeneous Rationality: The Cognitive Continuum, Emergence, and the Civilization–AI Spiral"
date: 2026-10-01 14:11:00 +0800
lang: en
permalink: /en/posts/from-reaction-to-heterogeneous-rationality/
alternate_url: /posts/from-reaction-to-heterogeneous-rationality/
categories: [AI, Cognition]
tags: [Artificial Intelligence, Cognitive Science, Complex Systems, Emergence, Rationality, Intuition, Collective Intelligence, Neuroscience, Epistemology]
description: "A framework for cognition that runs from single cells and nervous systems to individual reasoning, civilization, and AI. Reflex, intuition, and reason appear as macroscopic states of one continuous causal organization, shaped by nonlinear accumulation, abstraction, and externalization."
math: true
toc: true
comments: true
---

## Summary
{: #summary }

It is easy to describe "reflex, intuition, and reason" as three entirely distinct modes of cognition, and just as easy to line up "single cells, simple animals, humans, civilization, artificial intelligence" as a ladder running from lower to higher. These classifications, however, may be little more than coarse-graining: a simplification the observer makes in order to get a grip on complicated phenomena.

A more general picture runs as follows. Chemical reactions inside a cell, sensorimotor coupling in a single-celled organism, electrical signaling in plants, distributed nerve nets, large nervous systems, individual reasoning, language, culture, science, computers, and artificial intelligence can all be seen as realizations, at different scales, of a kind of **adaptive causal organization**. What they share is not that each has "reason" or "consciousness". What they share is that each takes in external and internal signals through its own internal states, and those states then shape what it does next. As memory, plasticity, integration, prediction, abstraction, recursion, communication, and externalization keep increasing, the system's macroscopic behavior becomes more and more complex.

The underlying variables can be continuous while behavior does not grow linearly. Thresholds, positive and negative feedback, network coupling, modularity, and structural reorganization can all make continuous change look, at the macroscopic level, like a series of roughly discrete "stages". Reflex, intuition, reason, language, and collective intelligence can therefore be understood as different regimes within one high-dimensional continuous space, rather than as several kinds of stuff separated by natural boundaries.

More important still: once a complex process settles into a stable macrostate, a higher-level system can treat it as a new simple component. A mass of perception can be compressed into an "object"; a multi-step chain of reasoning can be compressed into an "intuition"; the discoveries of a generation can be compressed into a "formula"; an entire algorithm can be compressed into a single function call. The new simple components are then combined with one another, and new complexity arises.

The result is a spiral that keeps climbing:

$$
\boxed{
\text{continuous accumulation}
\rightarrow
\text{nonlinear emergence}
\rightarrow
\text{stable abstraction}
\rightarrow
\text{new operable unit}
\rightarrow
\text{new complex combination}
}
$$

Human civilization pushed this cycle to a scale that spans many brains and many generations. Computers took part of explicit reasoning and outsourced it to mechanisms that run on their own. Large neural networks then compressed much of the knowledge and procedure that human culture had externalized back into artificial learning systems. If future AI goes on to form its own representations, primitives, and operators, there may arise a "heterogeneous rationality": one that is naturally simple from the AI's side and deeply foreign from ours.

That would put a new question to epistemology. The frontier of intelligence may lie less in "can it answer questions we already know how to ask" than in "can it create a new representable space, so that questions which could not previously be posed become questions for the first time".

## 1. The illusion of categories: the world is often continuous, yet behavior seems to have boundaries
{: #s1 }

Everyday language tends to describe the world in pairs:

- responsive / unresponsive;
- has memory / has no memory;
- rational / not rational;
- healthy / sick;
- intelligent / not intelligent;
- organism / machine;
- human thought / artificial computation.

These categories are useful, but the boundary of a category is not necessarily a boundary in the underlying structure of nature.

Threshold responses are a simple example. Suppose a system has a continuous internal variable $$q$$, and its observable behavior $$B$$ is approximately:

$$
B(q)=\frac{1}{1+e^{-k(q-q_c)}}
$$

When $$k$$ is large, $$q$$ needs to cross only a narrow band around $$q_c$$ for the outward behavior to swing from almost absent to almost fully present.

What the observer sees is:

$$
0\rightarrow 1
$$

Underneath, it may only be:

$$
0.47\rightarrow0.48\rightarrow0.49\rightarrow0.50\rightarrow0.51
$$

Such mechanisms are not limited to simple threshold functions. In dynamical systems, bifurcations, positive feedback, synchronization, competitive inhibition, hysteresis, and network critical phenomena can all turn a slowly changing control parameter into an abrupt shift of macroscopic state.

Neuroscience does have a body of work that describes brain dynamics in terms of criticality, but whether the brain generally operates at a precise critical point remains seriously contested. The cognitive continuum therefore does not need to rest on the strong hypothesis that "all intelligence is a physical phase transition". A more conservative claim, and one that is sufficient, is this:

$$
\boxed{
\text{continuous underlying change}
+
\text{nonlinear interaction}
\Rightarrow
\text{seemingly discrete macroscopic abilities}
}
$$

If reflex, intuition, and reason look like three different things, that need not be because nature drew three lines. It may be because different continuous capacities, once they interact, settle into a few macroscopic regimes that are easy to recognize.

## 2. The object of study: from "cognitive systems" to "adaptive causal organization"
{: #s2 }

Once the scope runs from single cells all the way to civilization and AI, the term "cognitive system" tends to assume too early that some of these things already have cognition. "Agent" tends to imply a single goal, intention, and clear boundaries. "System" is too broad to say much.

So a working concept is useful:

> **Adaptive causal organization**: a set of interacting units with internal states, such that external and internal signals can change those states, and the current state has a structured causal influence on future states and on the environment. As the organization acquires memory, plasticity, prediction, model formation, communication across units, or externalization, behavior closer to what we usually call "cognition" gradually appears.

In its minimal form:

$$
x_{t+1}=F_{\theta_t}(x_t,e_t)
$$

where:

- $$x_t$$: the system's internal state at time $$t$$;
- $$e_t$$: the current environment or external input;
- $$F_{\theta_t}$$: the state transition determined by the current structure $$\theta_t$$.

If the system can also act on the world:

$$
a_t=G_{\theta_t}(x_t,e_t)
$$

where $$a_t$$ is an action, an output, or an intervention in the environment.

If experience also changes the system itself:

$$
\theta_{t+1}
=
U(\theta_t,x_t,e_t,a_t,e_{t+1})
$$

then we have learning, or adaptation, in the broadest sense.

These equations do not try to reduce life, mind, and civilization to one set of microscopic equations. They offer a shared language: organizations at different scales can run on entirely different physical mechanisms and still share the abstract structure of state, transition, feedback, and update.

The research question can then move from:

> "Does it really count as cognitive?"

to:

> "How much state can it hold? Over how long a window can it integrate? Can it change its own transition rules? Can it form models? Can it pass intermediate states to other units? Can it model itself?"

## 3. Cognition is a high-dimensional continuous space rather than a single axis
{: #s3 }

"Intelligence from low to high" is still too one-dimensional.

What an organization can do depends on several variables at once. A conceptual vector can stand for them:

$$
\mathbf q
=
(M,\tau,P,I,H,A,R,E,B,\ldots)
$$

where the components might represent:

- $$M$$: capacity for retained internal state and memory;
- $$\tau$$: the time window of integration;
- $$P$$: plasticity and the ability to learn;
- $$I$$: the ability to integrate information across units;
- $$H$$: the depth of modules and hierarchy;
- $$A$$: the ability to abstract and compress;
- $$R$$: recursive modeling and self-modeling;
- $$E$$: externalization, transmission, and interoperability across systems;
- $$B$$: bandwidth of input, output, and internal communication.

Reflex, intuition, reason, language, and collective intelligence need not each be a new organ. They can be macroscopic phenomena that appear when $$\mathbf q$$ falls in different regions.

A fast local reflex, for instance, might have a short integration window, little abstraction, and almost no externalization. Expert intuition might combine highly trained internal representations with very brief online deliberation and fast mapping. Explicit reasoning needs intermediate states to be held, longer integration, compositional operations, and the ability to back out of errors. Collective reasoning further requires that different processors be able to exchange state.

A more general statement than "rational / irrational" is therefore:

> **Rationality is a macroscopic regime in a high-dimensional continuous space, not a new substance suddenly inserted into a system.**

## 4. Before neurons, life already had sophisticated control
{: #s4 }

Fixing the starting point of cognition at the neuron would miss the large amount of information processing and control that living systems already had.

### 4.1 Bacterial chemotaxis: molecular networks can approximate engineering control
{: #s4-1 }

Chemotaxis in *E. coli* is one of the classic examples.

The bacterium has no nervous system. Through receptors, protein signaling networks, and flagellar motors, it compares chemical changes in its surroundings and adjusts its run-and-tumble behavior, raising the odds that it moves toward a more favorable environment.

Adaptation in *E. coli* chemotaxis can even be understood as integral feedback control. Under sustained stimulation the system gradually returns to its baseline sensitivity, so that across a very wide range of background concentrations it keeps detecting *change* rather than absolute level.

This means certain control principles:

$$
\text{sensing}
\rightarrow
\text{state update}
\rightarrow
\text{feedback}
\rightarrow
\text{adaptation}
$$

long predate nervous systems.

None of this has to be called "reasoning", and it need not even be forced under the label "cognition". It already contains structural elements, though, that later and more complex cognition relies on heavily.

### 4.2 Paramecium: a single cell can have electrical excitability and sensorimotor transformation
{: #s4-2 }

Paramecium is a single-celled organism, yet it changes how it swims in response to mechanical, chemical, light, and temperature stimuli.

Its typical avoidance reaction is triggered by a Ca$$^{2+}$$-based action potential. A change in membrane potential opens voltage-gated calcium channels in the cilia, which reverses the direction of the ciliary beat. The paramecium briefly backs up, turns, and then swims forward again.

What matters is not whether we call this "thinking". What matters is:

> **A single cell can already link sensation, membrane potential, ion flow, and movement into a closed loop, with no need for neurons or a brain.**

### 4.3 The Venus flytrap: continuous accumulation can produce a near-binary "decision"
{: #s4-3 }

The Venus flytrap has no neurons, yet it uses electrical signals and Ca$$^{2+}$$ dynamics to coordinate its rapid closure.

![An open Venus flytrap with small trigger hairs on the inner lobes and longer tooth-like projections along the edges.](/assets/img/articles/cognition-flytrap.webp){: width="1527" height="1670" }
*The small hairs on the inner lobes receive the mechanical stimulation discussed here; the longer projections along the edges are a different structure. This photograph shows anatomy, not calcium dynamics over time. Photo: Noah Elhardt; [source](https://commons.wikimedia.org/wiki/File:Venus_Flytrap_showing_trigger_hairs.jpg), [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/). Converted to WebP without cropping.*

In the typical case, if two mechanical stimuli to the trigger hairs occur within about 30 seconds, the second one pushes cytosolic Ca$$^{2+}$$ up to the threshold associated with closure. If the second stimulus comes too late, the Ca$$^{2+}$$ signal from the first has already decayed, and the total is not enough to trigger closure.

Conceptually:

$$
C(t)<C_c
\Rightarrow
\text{stay open}
$$

$$
C(t)\ge C_c
\Rightarrow
\text{close}
$$

This example shows the whole "continuous underneath, discrete on the surface" pattern:

- Ca$$^{2+}$$ concentration is a continuous variable;
- the signal decays over time;
- two stimuli can be integrated over time;
- yet the final behavior is close to on/off.

So human phrases like "does it remember the first touch" or "did it make a decision" naturally suggest a binary, while the substrate may have no matching binary boundary at all.

Sources:

- [Yi et al., Robust perfect adaptation in bacterial chemotaxis through integral feedback control](https://authors.library.caltech.edu/records/sa6bx-35q11)
- [Responding to Chemical Gradients: Bacterial Chemotaxis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3320702/)
- [Integrative Neuroscience of Paramecium, a “Swimming Neuron”](https://www.eneuro.org/content/8/3/ENEURO.0018-21.2021)
- [Suda et al., Calcium dynamics during trap closure visualized in transgenic Venus flytrap](https://www.nature.com/articles/s41477-020-00773-1)
- [Hedrich & Kreuzer, Demystifying the Venus flytrap action potential](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19113)

## 5. The arrival of neurons was no "intelligence switch"
{: #s5 }

Neurons supply a very powerful mechanism for fast, plastic communication, but "having neurons" is not the same as "cognition suddenly being born".

The slime mould *Physarum polycephalum* has no nervous system, yet a substantial literature discusses its navigation, choice, habituation-like learning, spatial memory, and adaptive behavior. Whether these should be called cognition is still disputed on philosophical and definitional grounds. The dispute itself, though, suggests that treating the neuron as an absolute boundary is a poor choice.

A better picture is:

$$
\text{chemical networks}
\rightarrow
\text{electrical excitability}
\rightarrow
\text{specialized signaling cells}
\rightarrow
\text{nerve nets}
\rightarrow
\text{centralized nervous systems}
$$

Different evolutionary lineages need not pass through all these steps in the same order, and later steps are not necessarily "higher". The point is that changes in the speed, reach, plasticity, and organization of communication gradually widened the state space a system could coordinate.

Source: [Reid, Thoughts from the forest floor: a review of cognition in the slime mould *Physarum polycephalum*](https://link.springer.com/article/10.1007/s10071-023-01782-1)

## 6. Hydra: functional differentiation and behavioral sequences without a central brain
{: #s6 }

Hydra is an important case for seeing a continuum rather than a ladder.

Hydra has no centralized brain or ganglia. Its neurons number only in the hundreds to thousands, spread out in nerve nets. Yet whole-animal calcium imaging shows that these neurons are not one homogeneous mass. There are several functionally distinct, anatomically separable networks, each associated with behaviors such as contraction, elongation, radial contraction, and nodding.

More complex locomotion, such as somersaulting, also requires several movements to be coordinated in temporal order.

This shows that:

$$
\text{distributed nerve net}
\not\Rightarrow
\text{only a single reflex}
$$

Even in an architecture without a central brain, the following can gradually emerge:

- modularity;
- network specialization;
- sequence coordination;
- sensorimotor integration.

So between "reflex" and "multi-step behavior" there is no natural dividing line set by whether or not a brain is present.

Sources:

- [Dupre & Yuste, Non-overlapping neural networks in Hydra vulgaris](https://pmc.ncbi.nlm.nih.gov/articles/PMC5423359/)
- [Badhiwala et al., Multiple neuronal networks coordinate Hydra mechanosensory behavior](https://pmc.ncbi.nlm.nih.gov/articles/PMC8324302/)
- [Whole-body neural and muscle imaging in Hydra](https://pmc.ncbi.nlm.nih.gov/articles/PMC7452734/)

## 7. Evolution is no ladder of "hagfish = brainstem, amphioxus = cerebellum, fruit fly = cerebrum"
{: #s7 }

Mapping living species onto regions of the human brain can serve as an intuitive analogy, but it does not work as a theory of evolution.

Cyclostomes (lampreys and hagfishes) are not "vertebrates with only a brainstem". The 2023 lamprey brain cell atlas shows that jawless vertebrates already have the basic vertebrate regionalization into forebrain, midbrain, and hindbrain. At the same time, some cell types and structures that appeared later, such as the typical cerebellar cell types, may have formed only in the jawed-vertebrate lineage.

Amphioxus is not "cerebellum-level" either. Its central nervous system is relatively simple, but its anterior cerebral vesicle and neural tube carry a molecular blueprint related to vertebrate forebrain, midbrain, and hindbrain regionalization.

The fruit fly belongs to an entirely different evolutionary branch. The adult *Drosophila* brain connectome released in 2024 contains about 139,255 neurons and 54.5 million synapses, annotated into more than 8,400 cell types. A system like this can already support a rich repertoire that includes navigation, learning, choice, and social behavior.

The point of these examples is not to rank "levels of intelligence". It is this:

> **Completely different biological architectures can enter new behavioral regimes once their scale, connectivity, modularity, memory, and feedback increase.**

Evolution looks more like a branching design space than a single ladder running straight from lower forms up to humans.

Sources:

- [Lamanna et al., A lamprey neural cell type atlas illuminates the origins of the vertebrate brain](https://www.nature.com/articles/s41559-023-02170-1)
- [Albuixech-Crespo et al., Molecular regionalization of the developing amphioxus neural tube](https://pmc.ncbi.nlm.nih.gov/articles/PMC5396861/)
- [FlyWire Consortium, Neuronal wiring diagram of an adult brain](https://www.nature.com/articles/s41586-024-07558-y)

## 8. Why can quantitative change look like qualitative change?
{: #s8 }

Adding more units does not by itself guarantee more intelligence.

A million simple components that never communicate are not necessarily more capable than ten that are tightly coordinated.

Increasing scale does have two important effects, though.

First, the number of possible interactions grows quickly. Counting only potential pairwise connections, a system of size $$N$$ has:

$$
\frac{N(N-1)}{2}
$$

possible pairwise relations.

If each unit has only two states, the number of theoretical state combinations reaches:

$$
2^N
$$

Real biological systems never freely explore all of these states, and these expressions are not a formula in which "neuron count determines intelligence". They reveal only one thing:

> **As scale increases, the space of possible organizations grows far faster than scale itself.**

Second, once more units are organized through feedback, specialization, recurrence, hierarchy, and shared memory, the system can form stable macrostates that did not exist before.

A jump in capability is therefore better written as:

$$
\boxed{
\text{scale}
+
\text{topology}
+
\text{memory}
+
\text{plasticity}
+
\text{feedback}
+
\text{modularity}
+
\text{hierarchy}
\rightarrow
\text{nonlinear change in capability}
}
$$

"Quantitative change producing qualitative change", stated more precisely, does not mean simply adding more. It means:

> **Continuously increasing resources and connections make a new way of organizing stable for the first time.**

## 9. Genuine "levels" come from the formation of new operable units
{: #s9 }

When does a system actually acquire a new level?

Adding a component does not do it. A new level appears when a large number of low-level states can be used by a higher layer as a single stable unit.

Suppose the set of low-level primitives is $$S_n$$.

They are combined:

$$
C_n=\mathcal C(S_n)
$$

If some of the complex structures are stable enough, they can be compressed, abstracted, or coarse-grained:

$$
S_{n+1}=\Gamma(C_n)
$$

The formerly complex system $$C_n$$ then becomes a simple primitive $$S_{n+1}$$ at the next level.

So:

$$
\boxed{
S_n
\xrightarrow{\mathcal C}
C_n
\xrightarrow{\Gamma}
S_{n+1}
}
$$

And further:

$$
S_{n+1}
\rightarrow
C_{n+1}
\rightarrow
S_{n+2}
\rightarrow\cdots
$$

This is more accurate than "simple → complex → simple".

Because:

$$
S_{n+1}\neq S_n
$$

The simplicity that appears the second time is a new interface, formed once the complexity of the first level has been successfully encapsulated.

An "object" is an abstraction over a mass of sensory signals.

A "concept" is an abstraction over many instances.

A "function" is an abstraction over many program steps.

A "formula" is an abstraction over a great deal of derivation and experience.

An "expert judgment" may be an abstraction over years of learning.

A paper, a standard, an API, or a legal concept can likewise become a unit that higher-level cognition calls directly.

Levels, then, are not entirely lines drawn at the observer's whim. When a macrostate has a relatively stable interface and can be reused again and again by higher layers, it acquires real causal and operational standing.

## 10. A deep isomorphism with the "major evolutionary transitions", but with a wider scope
{: #s10 }

Research on the Major Evolutionary Transitions shows that the major transitions in the history of evolution often involve low-level units that could once exist relatively independently coming together, through cooperation, division of labor, interdependence, and coordination, to form a new higher-level individual.

Typical examples include:

- genes assembling into higher-level units of inheritance;
- prokaryotic components forming the eukaryotic cell;
- cells forming multicellular organisms;
- certain individuals forming highly integrated social collectives.

The analysis by West and colleagues links new individuality to cooperation, division of labor, interdependence, and communication; Maynard Smith and Szathmáry put more weight on changes in how information is stored and transmitted.

This shares a structure with the cognitive spiral:

$$
\text{low-level units that can act}
\rightarrow
\text{coordination and division of labor}
\rightarrow
\text{new higher-level unit}
$$

The cognitive spiral, though, can reach further.

The new unit need not be a biological individual that reproduces.

It can be:

- a neural module;
- a percept;
- a concept;
- a skill;
- a reasoning operator;
- a team;
- a scientific method;
- a program function;
- an AI agent;
- a human–machine collaboration network.

So the general principle may be:

$$
\boxed{
\text{low-level causal units}
\rightarrow
\text{stable coordination}
\rightarrow
\text{new operable causal unit}
}
$$

Sources:

- [West et al., Major evolutionary transitions in individuality](https://pmc.ncbi.nlm.nih.gov/articles/PMC4547252/)
- [Maynard Smith & Szathmáry, The major evolutionary transitions](https://www.nature.com/articles/374227a0)
- [Szathmáry, Toward major evolutionary transitions theory 2.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC4547294/)

## 11. Abstraction manufactures new macroscopic variables instead of blurring the world
{: #s11 }

When a person sees dogs of different coat colors, sizes, lighting, postures, and breeds, the underlying sensory states differ enormously.

If a cognitive system can map those states onto the same macrostate:

$$
x_1,x_2,\ldots,x_n
\xrightarrow{\Gamma}
\text{DOG}
$$

then "DOG" becomes a new operable variable.

Higher-level reasoning no longer has to reprocess every pixel; it can operate directly on:

$$
\text{DOG}
\rightarrow
\text{ANIMAL}
$$

This is the basic meaning of coarse-graining:

> Discard the microscopic differences that are irrelevant to the problem at hand, and keep the structure that is stable and useful at a given scale.

Abstraction is therefore a mechanism complex systems need in order to build higher-level computation, rather than a way for cognition to escape reality.

Herbert Simon discusses hierarchy and near-decomposability in *The Architecture of Complexity*; Philip Anderson's *More Is Different* stresses that higher scales develop effective laws of their own.

If a higher-level system had to re-track every microscopic state each time, it could never keep composing upward.

Sources:

- [Simon, The Architecture of Complexity](https://web.mit.edu/6.033/2006/wwwdocs/papers/protected/simon-complexity.pdf)
- [Anderson, More Is Different](https://doi.org/10.1126/science.177.4047.393)

## 12. Intuition and reason are different working modes on a compression–unfolding spectrum, not two separate systems
{: #s12 }

When an expert sees a familiar problem, what often happens is:

$$
x\rightarrow y
$$

There seems to be no intermediate reasoning.

Yet this single mapping $$x\rightarrow y$$ may already hold years of training compressed into the model's parameters:

$$
D_{\text{history}}
\rightarrow
F_\theta
$$

and then:

$$
y=F_\theta(x)
$$

Intuition can therefore be understood as follows:

> **A large amount of past computation has been compiled into the current model, so that online reasoning becomes very short.**

When a new problem goes beyond the reliable range of direct mapping, the system can add intermediate states:

$$
x
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
s_n
\rightarrow
y
$$

Computational depth is thus "unfolded" again, out of the model's parameters and onto time.

With practice, this long chain may be learned once more:

$$
(s_1,s_2,\ldots,s_n)
\rightarrow
F_{\theta'}
$$

Hence:

$$
\boxed{
\text{intuitionization}
\approx
\text{compressing computation into structure}
}
$$

$$
\boxed{
\text{explicit reasoning}
\approx
\text{unfolding computation over time}
}
$$

There is no natural break between the two.

The same task may call for explicit reasoning in a novice and be close to a reflex in an expert.

## 13. Reason is a macroscopic computational regime, not a mysterious module
{: #s13 }

If rationality has no sharp boundary, it can be redefined as a set of gradually strengthening capacities:

- intermediate states can be held long enough;
- those states can be read back;
- several operators can be composed in sequence;
- several hypothetical futures can be compared;
- immediate responses can be inhibited;
- states can be revised in light of evidence;
- the step where an error occurred can be located;
- some states can be externalized.

This gives a working definition:

> **Rationality is a macroscopic operating state that adaptive causal organization enters when it can carry out multi-step, constrained, correctable transformations on representations it is able to hold.**

The reasoning language at a given moment can be abstracted as:

$$
\mathcal R_t=(V_t,E_t,O_t,C_t)
$$

where:

- $$V_t$$: the objects that can be represented;
- $$E_t$$: the relations that can be recognized;
- $$O_t$$: the operators that can be executed;
- $$C_t$$: the constraints of consistency, evidence, goals, and verification.

Ordinary reasoning is:

$$
(\mathcal R_t,x)\rightarrow y
$$

Higher-order cognitive innovation rewrites $$\mathcal R_t$$ itself:

$$
\boxed{
\mathcal R_t
\rightarrow
\mathcal R_{t+1}
}
$$

This is why rationality should not be equated with any fixed system of formal logic.

Rationality at its highest includes:

> **revising the language one uses to reason.**

## 14. Affect is a value signal that governs the whole spectrum, not a separate track
{: #s14 }

Emotion and affect are more than "noise that shows up when reason fails".

Any adaptive system with finite resources has to settle:

- Which signals deserve attention?
- Which problems must be solved now?
- Which outcome is worth pursuing?
- Which direction should be avoided?
- Which memories need consolidating?
- Which computations are no longer worth their cost?

Emotion-related mechanisms can therefore be understood as:

$$
\text{value}
+
\text{salience}
+
\text{priority}
+
\text{action tendency}
$$

These signals adjust how the whole cognitive system allocates its resources.

Pessoa and others have long argued against simply mapping emotion and cognition onto mutually isolated brain regions. A better picture has multiple dynamic networks participating together across different tasks.

So the more general model is not:

$$
\text{affect}
\leftrightarrow
\text{reason}
$$

Instead it is:

$$
\text{state estimation}
+
\text{value estimation}
+
\text{resource allocation}
+
\text{action control}
+
\text{model updating}
$$

which together produce adaptive behavior.

Source: [Pessoa, On the relationship between emotion and cognition](https://www.nature.com/articles/nrn2317)

## 15. One of the great leaps: the system begins to model itself
{: #s15 }

An adaptive system can simply react to the outside world:

$$
\mathcal S
\rightarrow
a
$$

A more complex system can build a model of the world:

$$
M(W)
$$

Going further, the system itself can enter the model:

$$
M(\mathcal S,W)
$$

This creates a new feedback loop:

$$
\boxed{
\mathcal S
\rightarrow
M(\mathcal S)
\rightarrow
\Delta\mathcal S
}
$$

The system no longer changes its actions only in response to the world; it starts to reshape itself according to "a description of itself".

Humans studying their own brains, memories, and biases are one highly developed example.

Education research studying how to learn, organizations studying their own processes, philosophy of science studying scientific method, AI research studying how to improve AI training pipelines: all belong to the same kind of recursion:

$$
\text{system}
\rightarrow
\text{model of system}
\rightarrow
\text{system redesign}
$$

This kind of recursive self-modification is quite possibly an important source of cognitive acceleration.

## 16. The great leap of reason is being able to hand thinking to another system, more than "thinking better"
{: #s16 }

High-dimensional intuition has one huge limitation:

> **it can usually exist directly only inside the processor where it formed.**

An expert can judge within seconds:

> This design is wrong.

Others, however, cannot copy that expert's neural state.

If the expert unfolds the judgment into:

$$
r_1\rightarrow r_2\rightarrow r_3\rightarrow h
$$

others can:

- check $$r_1$$;
- dispute $$r_2\rightarrow r_3$$;
- replace one of the assumptions;
- continue computing onward from $$r_3$$.

The original:

$$
z_{\text{private}}
$$

is encoded as:

$$
z_{\text{private}}
\xrightarrow{E}
(r_1,r_2,\ldots,r_n)
$$

This conversion can be called:

$$
\boxed{\text{cognitive serialization}}
$$

It gives cognition:

- addressability;
- decomposability;
- citability;
- refutability;
- verifiability;
- modifiability;
- transferability.

The value of reason, then, goes beyond letting one person think a few more steps.

What matters more is this:

> **it lets the result of one processor's computation become the input of another processor.**

Mercier and Sperber's argumentative theory ties an important function of reasoning to producing and evaluating arguments; Shea and colleagues propose that explicit metacognition can be broadcast to coordinate supra-personal cognitive control.

Sources:

- [Mercier & Sperber, Why do humans reason?](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/why-do-humans-reason-arguments-for-an-argumentative-theory/53E3F3180014E80E8BE9FB7A2DD44049)
- [Shea et al., Supra-personal cognitive control and metacognition](https://pubmed.ncbi.nlm.nih.gov/24582436/)

## 17. Language, mathematics, and code are intermediate layers between different cognitive systems
{: #s17 }

No two human brains share the same neural state.

Humans and LLMs share even less of an implementation.

Even so, they may jointly operate on:

$$
A>B,\qquad B>C
$$

and arrive at:

$$
A>C
$$

Shared understanding therefore does not require:

$$
z_A=z_B
$$

It requires only that some task-relevant structure survive the translation.

Suppose system A contains:

$$
R(x_A,y_A)
$$

If there is a mapping $$\phi$$ that lets system B reconstruct:

$$
R'(\phi(x_A),\phi(y_A))
$$

then effective interoperability may arise.

Thus:

$$
\text{Brain}_A
\rightarrow
\text{language / math / diagram / code}
\rightarrow
\text{Brain}_B
$$

can be seen as a cognitive intermediate representation.

Language does not transmit one brain whole to another.

Over an extremely narrow bandwidth, it sends signals "sufficient for the other side to reconstruct part of the structure".

This also explains why:

- mathematics strives for low ambiguity;
- code strives to be executable;
- diagrams strive to make structure visible;
- scientific notation strives for reproducibility across people.

Each medium is in fact optimizing a different kind of structure-preserving transmission.

## 18. Once intermediate states can be passed on, the unit of cognition can extend beyond a single brain
{: #s18 }

A large problem can be broken into:

$$
T
\rightarrow
\{T_1,T_2,\ldots,T_n\}
$$

which different processors carry out:

$$
P_i(T_i)\rightarrow r_i
$$

and an integrating mechanism then combines:

$$
G(r_1,r_2,\ldots,r_n)\rightarrow R
$$

At this point the system's capability no longer equals the sum of individual capabilities:

$$
K_{\text{group}}
\neq
\sum_i K_i
$$

because overall performance also depends on:

- division of labor;
- communication bandwidth;
- shared representation;
- conflict resolution;
- memory;
- error correction;
- incentives;
- trust;
- interface quality.

Edwin Hutchins's research on distributed cognition treats the navigation team, its instruments, charts, procedures, and the flow of information among the people as a single cognitive system.

Transactive memory theory describes how a team forms a distributed memory through "who knows what": members need not each remember everything, as long as they can locate, trust, and coordinate different kinds of expertise.

So the bottleneck of group intelligence is often less this:

> People aren't smart enough.

than this:

> **The result in one brain cannot reliably become the input to another.**

Sources:

- [Hutchins, Cognition in the Wild](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)
- [Peltokorpi & Hood, Communication in Theory and Research on Transactive Memory Systems](https://onlinelibrary.wiley.com/doi/full/10.1111/tops.12359)

## 19. Writing lets cognition outlive a lifetime; culture lets operators themselves be inherited
{: #s19 }

Speech roughly accomplishes:

$$
\text{Brain}_A
\rightarrow
\text{Brain}_B
$$

Writing and other external memory accomplish:

$$
\text{Brain}_A(t_0)
\rightarrow
\text{external representation}
\rightarrow
\text{Brain}_B(t_0+\Delta t)
$$

where $$\Delta t$$ can far exceed an individual lifespan.

What matters goes beyond "data being preserved."

Civilization also preserves:

- methods of classification;
- concepts;
- mathematical operators;
- experimental designs;
- reasoning procedures;
- proof techniques;
- debugging methods;
- legal institutions;
- organizational structures;
- programs;
- APIs.

So cultural transmission need not be simply:

$$
\text{answer}
\rightarrow
\text{next generation}
$$

It can be:

$$
\boxed{
\text{cognitive operator}
\rightarrow
\text{next generation}
}
$$

Heyes's theory of *Cognitive Gadgets* holds that culture shapes how we think as well as what we think; some higher cognitive mechanisms may form and spread across generations through social learning.

Muthukrishna and Henrich's collective brain view treats innovation as an emergent product of serendipity, recombination, and incremental improvement within social networks, rather than the isolated output of a few geniuses.

Sources:

- [Heyes, Précis of Cognitive Gadgets](https://doi.org/10.1017/S0140525X18002145)
- [Muthukrishna & Henrich, Innovation in the collective brain](https://pmc.ncbi.nlm.nih.gov/articles/PMC4780534/)

## 20. Science is a civilization-scale cognitive control loop
{: #s20 }

Many of the formal requirements of scientific institutions can be reread as engineering for distributed cognition.

### Methods sections
{: #s20-1 }

Externalize the computation so that another processor can rerun it.

### Citation
{: #s20-2 }

Mark the source of a given calculation, observation, or theory.

### Replication
{: #s20-3 }

Have an independent processor try to rebuild the same result.

### Peer review
{: #s20-4 }

Have other processors error-check the reasoning trace and the evidence.

### Mathematics
{: #s20-5 }

Reduce ambiguity of representation.

### Standard units
{: #s20-6 }

Establish a shared coordinate system.

### Instrument calibration
{: #s20-7 }

Make the outputs of different measurement systems comparable.

### Databases and version control
{: #s20-8 }

Establish persistent state across time.

Science, then, is more than "a group of rational people."

It is a civilization-scale control architecture built from:

$$
\boxed{
\text{representation}
+
\text{memory}
+
\text{verification}
+
\text{error correction}
+
\text{coordination}
}
$$

Seen this way, the scientific method and the nervous system are different things, yet they share a more abstract problem:

> How do you build reliable knowledge among noisy, limited, local processors?

## 21. Computers: the first time humans fixed large numbers of explicit operators directly in the outside world
{: #s21 }

The deepest change computers brought goes beyond speed.

They let humans fully formalize certain kinds of reasoning:

$$
\text{COMPARE},\quad
\text{ADD},\quad
\text{BRANCH},\quad
\text{LOOP},\quad
\text{SEARCH}
$$

Once a procedure is written:

$$
\text{explicit reasoning}
\rightarrow
\text{formalization}
\rightarrow
\text{program}
\rightarrow
\text{automatic execution}
$$

people no longer have to think through the same operation each time.

This shares an important abstract similarity with biological skill learning:

$$
\text{expensive high-level computation}
\rightarrow
\text{encapsulation}
\rightarrow
\text{low-cost primitive}
$$

Computers can therefore be seen as a vast external automatic layer that civilization has built.

A CPU is no brainstem, and a program is no spinal reflex; yet both display the same architectural principle:

> **Complexity that has been mastered can sink downward and become a stable mechanism that no longer needs high-level deliberation.**

## 22. The history of AI replays "explicit rules, high-dimensional learning, recombination"
{: #s22 }

The history of artificial intelligence is no single line in which "symbolic AI was replaced by neural AI." The two approaches ran in parallel for a long time, and as early as the McCulloch–Pitts neuron there was an attempt to connect neural models with logic.

Functionally, though, an important cycle is still visible.

### Explicit rules
{: #s22-1 }

Humans write directly:

$$
\text{if }A\text{ then }B
$$

### Expert systems
{: #s22-2 }

Large amounts of explicit knowledge and inference rules are piled up into knowledge bases.

### Neural networks
{: #s22-3 }

The system learns representations from data:

$$
D\rightarrow F_\theta
$$

### LLMs and agentic systems
{: #s22-4 }

High-dimensional neural models start drawing again on:

- intermediate reasoning;
- search;
- code execution;
- calculators;
- databases;
- symbolic solvers;
- external memory;
- other agents.

So modern AI is not heading toward "neural networks finally returning to simple logic."

It looks more like:

$$
\boxed{
\text{high-dimensional learning}
+
\text{sequential computation}
+
\text{precise tools}
+
\text{external memory}
+
\text{cross-agent collaboration}
}
$$

Different computational regimes are being placed back into a single architecture.

Toolformer shows how a model can learn when to call external tools; AlphaGeometry combines neural proposals with symbolic deduction; DreamCoder compresses recurring program structures into new symbolic abstractions and adds them to its own language.

Sources:

- [Toolformer](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)
- [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5)
- [DreamCoder](https://pubmed.ncbi.nlm.nih.gov/37271169/)

## 23. LLMs are a special event: culturally externalized reason compressed back into an artificial neural network
{: #s23 }

The human world of text is unlike ordinary environmental data.

Books, papers, mathematics, code, law, textbooks, and arguments contain a great deal of cognitive structure that humans have already externalized.

Training a large language model therefore takes a very particular form:

$$
\text{human cognition}
\rightarrow
\text{language / code / symbols}
\rightarrow
\text{training data}
\rightarrow
F_\theta
$$

That is:

$$
\boxed{
\text{explicit cognition unfolded by humans over millennia}
\rightarrow
\text{recompressed into an artificial neural network}
}
$$

The model then uses reasoning tokens, tools, and search to unfold part of the computation again:

$$
F_\theta
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
a
$$

This forms a very clear sequence:

$$
\boxed{
\text{unfolding}
\rightarrow
\text{cultural preservation}
\rightarrow
\text{artificial compression}
\rightarrow
\text{re-unfolding}
}
$$

AI, then, may be entering the same cross-generational feedback loop as the human cognitive spiral, instead of forming a separate story outside it.

## 24. What reasoning tokens mean: parameters cannot fully replace time
{: #s24 }

Much of a neural network's capability is stored in its parameters.

But not every computation suits a single forward mapping.

Explicit or external intermediate states provide:

$$
s_{t+1}
=
F_\theta(x,s_{\le t})
$$

The same $$\theta$$ can be reused, producing more serial computation.

This reveals an important trade-off:

$$
\boxed{
\text{stored structure}
\rightleftarrows
\text{online computation}
}
$$

or equivalently:

$$
\text{parameters / learned intuition}
\rightleftarrows
\text{time / reasoning depth}
$$

Large numbers of parameters can precompile common patterns; more test-time steps can handle new combinations that require sequential dependence.

The text output of Chain-of-Thought does not guarantee a faithful account of all the causal mechanisms inside the model, so "it wrote out a rationale" should not be equated with "this is the whole of its actual thinking." Still, intermediate states have real value as a computational scratchpad that can be read back.

Sources:

- [Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html)
- [Li et al., Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](https://arxiv.org/abs/2402.12875)

## 25. What is "simple" for humans is not necessarily simple for intelligence in general
{: #s25 }

The primitives humans grasp naturally are closely tied to the human body, senses, evolutionary history, and cultural history.

Humans readily form:

- objects;
- paths;
- containers;
- before and after;
- up and down;
- linear time;
- agents;
- causation;
- quantity.

But are these the most natural basis that every possible intelligence would adopt?

Nothing guarantees it.

Suppose the cost of describing some structure $$z$$ in human representation is:

$$
L_H(z)
$$

and its cost in some AI representation is:

$$
L_A(z)
$$

It is entirely possible that:

$$
\boxed{
L_H(z)\gg L_A(z)
}
$$

That is:

> A simple object that is close to a primitive for an AI may need an extremely long description once translated into human concepts.

The reverse can also hold:

$$
L_A(y)\gg L_H(y)
$$

"Simplicity" itself is therefore relative to architecture and to representation.

This does not make truth wholly relative. The world still constrains which models work.

What is relative is this:

> **How complex a language a given effective structure requires in order to be expressed, for different cognitive architectures.**

Source: [Stanford Encyclopedia of Philosophy, Simplicity](https://plato.stanford.edu/entries/simplicity/)

## 26. Future AI may form its own cognitive basis
{: #s26 }

The truly major breakthrough of future AI may lie less in using operators humans already know at greater speed than in forming its own:

$$
V_A,\quad E_A,\quad O_A
$$

namely:

- AI-native objects;
- AI-native relations;
- AI-native operators.

Suppose it forms latent variables:

$$
u_1,u_2,\ldots,u_k
$$

along with operations that are very natural to it:

$$
u_1\star u_2=u_3
$$

For the AI, the computational cost of $$\star$$ may be very low.

Yet fully translating it into human primitives might take an enormous number of steps.

At that point:

$$
\mathcal R_A
=
(V_A,E_A,O_A,C_A)
$$

and the human:

$$
\mathcal R_H
=
(V_H,E_H,O_H,C_H)
$$

are no longer just "the same rationality running at different speeds."

They may instead be:

$$
\boxed{
\mathcal R_A
\not\approx
\mathcal R_H
}
$$

This is heterogeneous rationality in the full sense.

## 27. "AI axioms" call for first separating primitives, operators, and formal axioms
{: #s27 }

"AI may have its own axioms" is a powerful intuition, but formally it needs to be split into three levels.

### AI-native primitives
{: #s27-1 }

The AI forms a set of latent objects that are unnatural to humans.

### AI-native operators
{: #s27-2 }

The AI discovers a set of transformations that operate effectively on those objects.

### AI-native formal axioms
{: #s27-3 }

Only when certain objects, relations, and inference rules are explicitly formalized can we strictly speak of a new axiom system.

So what is most likely to happen first is not:

> AI announces a few axioms humans cannot understand.

It is more likely this:

> **AI gradually forms an internal scientific language for which humans lack natural corresponding concepts.**

Later, if humans ask for formal proof or symbolic translation, the AI may then compile part of that language's structure into a formal system.

## 28. Current AI already shows weak precursors of "new solutions", but this is not yet heterogeneous rationality
{: #s28 }

AlphaTensor found new matrix multiplication algorithms.

AlphaDev found new low-level sorting routines, some of which were integrated into an actual C++ library implementation.

FunSearch found new constructions and heuristics for mathematical problems such as the cap set problem, and for bin packing.

These results show that:

$$
\text{AI search}
\rightarrow
\text{human-unknown solution}
$$

can happen.

But they still sit mainly within:

$$
\boxed{
\text{human-defined problem}
+
\text{human-defined scoring/verification}
+
\text{AI searches for solutions}
}
$$

The deeper turn would be:

$$
\text{AI changes the representation space itself}
$$

That is, the AI would go beyond answering:

> What is the answer to this problem?

and begin to discover:

> This problem should never have been described in the variables humans currently use.

Sources:

- [AlphaTensor](https://www.nature.com/articles/s41586-022-05172-4)
- [AlphaDev](https://www.nature.com/articles/s41586-023-06004-9)
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)

## 29. Two kinds of unknown: not knowing the answer, and not knowing how to form the question
{: #s29 }

The first kind of unknown:

$$
f(x)=?
$$

The representation already exists; only the value is missing.

It can be written as:

$$
\text{known representation}
+
\text{unknown answer}
$$

The second kind of unknown runs deeper.

There may be some stable structure:

$$
R^*(x_1,x_2,\ldots,x_n)
$$

yet the current cognitive system:

- has no sense that can tell it apart directly;
- has no variable to represent it;
- has no concept to name it;
- has no operator to act on it;
- has no experimental design that can isolate it.

In that case:

$$
\boxed{
\text{representation itself is missing}
}
$$

Here, "more data" does not necessarily solve the problem.

What is needed is:

$$
V_t\rightarrow V_{t+1}
$$

or:

$$
E_t\rightarrow E_{t+1}
$$

or:

$$
O_t\rightarrow O_{t+1}
$$

That means changing what can be seen, what relations can be represented, and what operations can be performed.

So beyond the boundary of knowledge there also lie:

> **"Unaskable unknowns."**

These may be far larger than the "known unknowns".

## 30. Why do scientific revolutions so often come with new mathematics and new vocabulary?
{: #s30 }

If a problem were only a matter of finding an answer in a fixed search space, more compute and more data should always yield gradual improvement.

Yet the history of science keeps producing a different kind of event:

> Under a new representation, an old problem suddenly becomes a different problem.

Introducing:

- complex numbers;
- calculus;
- coordinates;
- fields;
- entropy;
- genes;
- spacetime;
- information;

did more than give a known object one more name.

They changed:

$$
V,\quad E,\quad O
$$

so that structures which could not be expressed concisely before became operable for the first time.

Deep creativity, then, may lie less in:

$$
\text{search faster in }\mathcal R_t
$$

than in:

$$
\boxed{
\mathcal R_t
\rightarrow
\mathcal R_{t+1}
}
$$

Ohlsson's work on insight problem solving emphasizes representation restructuring; Gentner's structure-mapping theory explains how analogy forms new abstractions through relational mapping across domains.

Sources:

- [Ohlsson, Restructuring revisited](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9450.1984.tb01005.x)
- [Gentner, Structure-Mapping: A Theoretical Framework for Analogy](https://www.sciencedirect.com/science/article/abs/pii/S0364021383800093)

## 31. What happens to science when understanding and reliability come apart?
{: #s31 }

Suppose an AI builds a theory $$T_A$$.

It can:

- predict phenomena not yet observed;
- design new materials;
- propose new drugs;
- produce highly reliable engineering designs;
- derive reproducible experiments;
- keep passing external validation.

But:

$$
L_H(T_A)
$$

is enormous, and humans can hardly reconstruct its internal representation in full.

At that point "knowing" splits into different levels.

### Operational knowing
{: #s31-1 }

Knowing how to use the output.

### Predictive knowing
{: #s31-2 }

Knowing in which domains it predicts reliably.

### Verificational knowing
{: #s31-3 }

Knowing how to check the results with independent tests.

### Representational understanding
{: #s31-4 }

Humans themselves hold a cognitive representation short enough to reconstruct the "why".

In the future we may see:

$$
\text{operational knowledge}\approx 1
$$

$$
\text{verification}\approx 1
$$

but:

$$
\text{human representational understanding}\ll 1
$$

"Understanding" and "reliable knowledge" would then no longer always move together.

## 32. Shared verification may be more general than shared intuition
{: #s32 }

Two cognitive architectures that share the same primitives can build common understanding through explanation.

But if:

$$
V_H\neq V_A,\qquad O_H\neq O_A
$$

then requiring the AI to explain everything "until humans fully grasp it intuitively" may carry a structural cost.

The underlying interface for working together may then shift to:

$$
\text{formal proof}
$$

$$
\text{machine-checkable certificate}
$$

$$
\text{reproducible experiment}
$$

$$
\text{independently testable prediction}
$$

$$
\text{executable artifact}
$$

That is:

$$
\boxed{
\text{shared intuition}
\text{ is not required; }
\text{shared verification}
\text{ can serve as a lower-level common interface}
}
$$

This does not mean giving up on explainability.

It places explainability inside a larger question:

> **Between two different cognitive bases, which structures must be translated, and which results need only be independently verified?**

## 33. Which long-standing puzzles can this framework answer anew?
{: #s33 }

### 1. Why is higher-order reasoning so slow?
{: #s33-1 }

If one function of explicit reasoning is to squeeze highly parallel, high-dimensional cognition into a serial channel that can hold intermediate states, then the loss of speed is a structural price.

It gives up:

$$
\text{parallel throughput}
$$

in exchange for:

$$
\text{serial depth}
+
\text{inspectability}
+
\text{revisability}
+
\text{transmissibility}
$$

The slowness of reason may therefore be less a plain defect than the cost of turning cognition into objects that can be composed, inspected, and handed over.

### 2. Why do experts know the answer yet often cannot say why?
{: #s33-2 }

If learning compresses a long procedure into:

$$
x\rightarrow y
$$

then asking an expert to explain amounts to asking for:

$$
y\rightarrow\text{reconstruct}(s_1,s_2,\ldots,s_n)
$$

But compression does not guarantee that the original training history is preserved.

Hence:

$$
\boxed{
\text{competence}
\neq
\text{verbalizable reasoning trace}
}
$$

This also explains why being able to do something and being able to teach it are different abilities.

### 3. Why can education let ordinary people use the best thinking of centuries past within a dozen or so years?
{: #s33-3 }

Education does not ask students to retrace the whole discovery path. It transmits directly what civilization has already compressed:

$$
\text{concepts}
+
\text{operators}
+
\text{notations}
+
\text{problem representations}
$$

Thus:

$$
\text{costly historical discovery}
\rightarrow
\text{textbook compression}
\rightarrow
\text{rapid installation in individuals}
$$

The advantage of civilization lies in sparing each new generation from starting at zero, rather than in every generation becoming Newton again.

### 4. Why can an organization made of smart people still be very stupid?
{: #s33-4 }

Because group intelligence depends on more than node intelligence.

If:

- representations are inconsistent;
- intermediate results cannot be handed over;
- responsibilities are unclear;
- who knows what is opaque;
- errors cannot be located;
- information is blocked by incentives or hierarchy;

then adding more smart people may only add noise.

The bottleneck of collective intelligence may lie first in the interface, before IQ.

### 5. Why do so many scientific revolutions come with new mathematics and new vocabulary?
{: #s33-5 }

Because some problems suffer from inadequate representation rather than insufficient data.

If the old language cannot express a new structure concisely, a new primitive must be created first.

So a scientific revolution often looks less like:

> filling a few more rows into the same table.

and more like:

> switching to a different table.

### 6. Why might using tools be the core of intelligence rather than a compromise of it?
{: #s33-6 }

If a calculator already handles a subproblem reliably, having costly general-purpose cognition re-simulate it is not necessarily more intelligent.

A mature system should learn:

$$
\text{problem}
\rightarrow
\text{best available operator}
$$

One important capacity of intelligence is knowing when to reduce a problem to a verified primitive, instead of "doing everything yourself".

### 7. Why might explainable AI face a structural ceiling?
{: #s33-7 }

If AI and humans used the same set of primitives and the model were simply too large, we could in principle expect ever better translation tools.

But if:

$$
V_A\neq V_H
$$

and:

$$
O_A\neq O_H
$$

then explanation goes beyond "shortening a long answer": it means compiling an object from one cognitive space into another.

A complete translation may involve unavoidable inflation:

$$
L_H(x)\gg L_A(x)
$$

Some of the difficulties of interpretability may therefore stem from representation mismatch, rather than from engineering that simply has not been done well yet.

### 8. Why might AI's greatest scientific breakthroughs lie outside answering the questions humans pose?
{: #s33-8 }

If the binding constraint comes from representation, AI's greatest contribution may first be:

$$
\text{new variables}
+
\text{new invariants}
+
\text{new operators}
+
\text{new problem spaces}
$$

That is, posing questions humans were previously unable to form.

The answers come second.

## 34. The framework yields several more striking implications
{: #s34 }

### Implication 1: the main product of a civilization may be new forms of "simple" rather than knowledge
{: #s34-1 }

The more mature a civilization becomes, the more primitives its successors can use directly.

Progress in civilization can therefore be roughly understood as:

$$
\Delta \text{Civilization}
\sim
\Delta \text{Reusable Primitives}
$$

Growth in the amount of knowledge is only one part of this.

What changes the abilities of the next generation is which complexities have already been encapsulated behind simple interfaces.

### Implication 2: language matters because it partitions computation, beyond describing the world
{: #s34-2 }

If a language could carry only final answers, collective thinking would remain limited.

A truly powerful language must be able to represent:

- assumption;
- evidence;
- uncertainty;
- dependency;
- counterfactual;
- error;
- procedure.

So the cognitive power of a language depends on more than its vocabulary. It turns on whether the language can carry intermediate computation.

### Implication 3: rationality may be interoperability first, and correctness second
{: #s34-3 }

A person can reason with perfect logic from a false premise and arrive at an entirely false conclusion.

So what is special about reason need not be defined first as "reaching the truth".

Its deeper feature may be this:

> **It turns cognition into an object that can be checked, handed over, and recombined.**

Truth further depends on:

$$
\text{representation}
+
\text{evidence}
+
\text{verification}
+
\text{world feedback}
$$

### Implication 4: individual "independent thinking" has always been an extension of collective thinking
{: #s34-4 }

Most of the high-level primitives in a modern person's head came from other people.

A more accurate form for individual reasoning may therefore be, instead of:

$$
R(x)
$$

this:

$$
R(x\mid C)
$$

where $$C$$ stands for the language, concepts, mathematics, methods, literature, tools, and institutions that civilization supplies.

What we call "independent thinking" is usually individual recombination performed on top of a large body of collective priors.

### Implication 5: joint human–machine cognition may form a new unit of evolution
{: #s34-5 }

When AI becomes, all at once:

- a learner of cultural data;
- a reasoning executor;
- a dispatcher of tools;
- a searcher;
- a producer of new content;
- a cognitive interface for humans;

the whole loop becomes:

$$
\text{human culture}
\rightarrow
\text{AI learning}
\rightarrow
\text{AI reasoning}
\rightarrow
\text{new artifacts}
\rightarrow
\text{human learning}
\rightarrow
\text{new culture}
$$

So the unit of the next round of cognitive evolution may be neither:

$$
\text{human}
$$

nor:

$$
\text{AI}
$$

but the shared feedback system formed by:

$$
\boxed{
\text{human}
+
\text{culture}
+
\text{tools}
+
\text{AI}
}
$$

taken together.

## 35. Testable predictions
{: #s35 }

If this framework has theoretical value, it should generate predictions that can be tested.

### Prediction 1: capacity boundaries should be more continuous than traditional categories suggest
{: #s35-1 }

If "reflex, intuition, and reason" are coarse-grained regimes, then fine-grained tasks should reveal many intermediate forms, instead of all behavior falling naturally into a few clusters.

Measurable variables include:

- memory horizon;
- intermediate-state persistence;
- response latency;
- counterfactual depth;
- transfer;
- externalizability.

### Prediction 2: growth in macroscopic capacities should often be highly nonlinear
{: #s35-2 }

As memory, communication, recurrence, or representation capacity increases, performance on some tasks may rise abruptly within a particular range.

This does not require all tasks to share the same critical point.

More likely:

$$
q_c=q_c(\text{task},\text{architecture},\text{environment})
$$

### Prediction 3: an important new abstraction should both lower description cost and raise reuse
{: #s35-3 }

A good new primitive does more than shorten one answer.

For a set of problems $$\{x_i\}$$, a new language should make:

$$
\sum_i L_{\text{new}}(x_i)
<
\sum_i L_{\text{old}}(x_i)
$$

and improve cross-task transfer.

### Prediction 4: the more complex a multi-person task, the more the quality of intermediate representations matters
{: #s35-4 }

Groups that exchange only final answers should find it harder to scale their capacity with headcount.

Groups that can exchange assumptions, confidence, dependencies, intermediate results, and provenance should achieve better error localization and parallelization.

### Prediction 5: as the cognitive bases of AI and humans diverge, verifiability will matter more than natural-language explanation
{: #s35-5 }

If representation mismatch increases:

$$
d(\mathcal R_H,\mathcal R_A)\uparrow
$$

then the cost of full translation should rise.

Formal proof, independent experiment, certificates, and cross-system verification should gain relative value.

### Prediction 6: strong AI discovery systems will gradually shift from "solving problems" to "rewriting representations"
{: #s35-6 }

If future systems draw their capability only from larger search, they will increasingly run into costs under a fixed representation.

Stronger systems should more and more often learn:

$$
\text{new primitives}
+
\text{new operators}
+
\text{new decompositions}
$$

instead of simply searching the old space faster.

## 36. What this framework cannot claim
{: #s36 }

To avoid turning a general framework into an overconfident law of nature, a few boundaries need to stay in place.

### More complexity does not always mean more intelligence
{: #s36-1 }

Scale can add noise, fragility, and coordination cost.

### Emergence is not always a thermodynamic phase transition
{: #s36-2 }

"Phase transition" is a useful analogy, but it should be used strictly only where the corresponding mathematics and evidence exist.

### Living species should not be lined up as an evolutionary ladder leading to humans
{: #s36-3 }

Different species represent different evolutionary branches and different architectures.

### Functional analogies in cognition should not be mistaken for the same neural implementation
{: #s36-4 }

A reflex, a CPU branch, and an LLM tool call may share an abstract control structure, yet their implementations are entirely different.

### Differences in representation between humans and AI should not be equated with "AI has surpassed humans"
{: #s36-5 }

Heterogeneous does not mean superior. Different bases may each have strengths and blind spots in different domains.

### "Cannot be understood" should not be treated as "need not be verified"
{: #s36-6 }

The opposite holds: the larger the representation mismatch, the stricter external validation should be.

## 37. The overall model: cognition as a spiral that keeps forming new scales, rather than a ladder
{: #s37 }

The most basic adaptive causal organization can be written as:

$$
x_{t+1}=F_{\theta_t}(x_t,e_t)
$$

When plasticity appears:

$$
\theta_{t+1}=U(\theta_t,\text{experience})
$$

When representations can form stably:

$$
x\rightarrow z
$$

When intermediate states can unfold:

$$
z
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
$$

When these states can be externalized:

$$
s_i^{(A)}
\rightarrow
r_i
\rightarrow
s_i^{(B)}
$$

cognition across individuals takes shape.

When externalized representations can be preserved across time:

$$
r(t_0)
\rightarrow
r(t_0+\Delta t)
$$

cumulative culture takes shape.

When a repeatedly successful procedure is compressed:

$$
(s_1,s_2,\ldots,s_n)
\rightarrow
o_{\text{new}}
$$

a new primitive takes shape.

The whole can therefore be written as:

$$
\boxed{
\begin{aligned}
\text{reaction and control}
&\rightarrow
\text{state retention and learning}\\
&\rightarrow
\text{prediction and abstraction}\\
&\rightarrow
\text{multi-step composition}\\
&\rightarrow
\text{externalization and sharing}\\
&\rightarrow
\text{collective computation}\\
&\rightarrow
\text{cultural compression}\\
&\rightarrow
\text{new primitives}\\
&\rightarrow
\text{new reaction, learning, and reasoning}
\end{aligned}
}
$$

This is neither a ladder of species evolution nor a ladder of brain regions.

What it describes is:

> **how the same kind of organizing principle recurs across different substrates, different scales, and different historical paths.**

## 38. Final thesis: rationality is one macroscopic stable state in a vast space of possibilities
{: #s38 }

If the framework above holds, several common intuitions need to be rearranged.

First, reflex is not the opposite of reason.

It is the regime some computations reach once they have been compressed, localized, and made low-latency.

Second, intuition is not a lower form that lacks reasoning.

It may be a fast model compiled from a great deal of past reasoning, learning, and experience.

Third, reason is not a new substance that suddenly appears.

It may be a macro-regime that forms once memory, recurrence, abstraction, composition, error correction, and state persistence have accumulated.

Fourth, language does more than express thought.

It lets intermediate computation travel between processors.

Fifth, a civilization is more than a collection of many people.

It is a distributed cognitive organization with external memory, specialized nodes, shared representations, verification protocols, and the capacity to remake itself.

Sixth, the computer is more than a tool.

It sinks part of civilization's explicit operators down into an external automatic layer.

Seventh, AI is more than one more "artificial brain" made by civilization.

It is absorbing the cognitive library humans have externalized and adding new learned representations, search, tool use, and machine-speed iteration, forming a new feedback path.

So the most general structure is not:

$$
\text{reflex}
\rightarrow
\text{intuition}
\rightarrow
\text{reason}
\rightarrow
\text{civilization}
\rightarrow
\text{AI}
$$

It is this:

$$
\boxed{
\text{continuous capacity space}
\xrightarrow{\text{nonlinear organization}}
\text{macroscopic regime}
\xrightarrow{\text{abstraction and encapsulation}}
\text{new primitive}
\xrightarrow{\text{recombination}}
\text{larger capacity space}
}
$$

There is no reason this cycle should stop with humans.

## 39. Conclusion: the frontier of intelligence lies in creating new "thinkable worlds"
{: #s39 }

The most important achievement of human civilization may lie less in how many answers it has accumulated than in its steady expansion of:

$$
\text{representable world }V
$$

$$
\text{recognizable relations }E
$$

$$
\text{usable operations }O
$$

$$
\text{verifiable constraints }C
$$

Every deep cognitive breakthrough may be changing:

$$
\mathcal R=(V,E,O,C)
$$

The next generation therefore knows more, and also holds a larger "thinkable space".

Human history has done this again and again.

AI may, for the first time, let it continue on another substrate, at a different speed, with a different perceptual range, a different scale of memory, and a different representation bias.

If a future AI forms:

$$
\mathcal R_A
$$

and it diverges sharply from the human:

$$
\mathcal R_H
$$

then humanity will face, for the first time and at scale, a kind of:

> cognition that works on the world yet does not rest on what humans naturally find "simple".

The watershed will be whether AI begins to create the following, more than whether it can answer more exam questions:

- primitives humans do not have;
- relations humans do not have;
- operators humans do not have;
- problem spaces humans do not have.

At that point, the deepest question is no longer:

> "Does it think like a human?"

It becomes:

> **When two cognitive systems differ even on what counts as simple, how do they build a knowledge interface good enough to exchange, verify, and accumulate together?**

The future of cognition may therefore look less like a straight line toward some ultimate rationality.

It looks more like a spiral that keeps unfolding:

$$
\boxed{
\text{world}
\rightarrow
\text{reaction}
\rightarrow
\text{learning}
\rightarrow
\text{abstraction}
\rightarrow
\text{sharing}
\rightarrow
\text{new tools}
\rightarrow
\text{new cognition}
\rightarrow
\text{new visibility of the world}
}
$$

And with each turn, the answers are only part of what changes.

What changes is:

> **what can become a question.**

## References and further reading
{: #refs }

### Non-neural and early sensorimotor control
{: #refs-1 }

1. Yi, T.-M., Huang, Y., Simon, M. I., & Doyle, J. *Robust perfect adaptation in bacterial chemotaxis through integral feedback control*.
   <https://authors.library.caltech.edu/records/sa6bx-35q11>

2. Sourjik, V., & Wingreen, N. S. *Responding to Chemical Gradients: Bacterial Chemotaxis*.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC3320702/>

3. *Integrative Neuroscience of Paramecium, a “Swimming Neuron”*.
   <https://www.eneuro.org/content/8/3/ENEURO.0018-21.2021>

4. Suda, H. et al. *Calcium dynamics during trap closure visualized in transgenic Venus flytrap*. Nature Plants, 2020.
   <https://www.nature.com/articles/s41477-020-00773-1>

5. Hedrich, R., & Kreuzer, I. *Demystifying the Venus flytrap action potential*. New Phytologist, 2023.
   <https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19113>

6. Reid, C. R. *Thoughts from the forest floor: a review of cognition in the slime mould Physarum polycephalum*. Animal Cognition, 2023.
   <https://link.springer.com/article/10.1007/s10071-023-01782-1>

### Simple nervous systems and brain evolution
{: #refs-2 }

7. Dupre, C., & Yuste, R. *Non-overlapping neural networks in Hydra vulgaris*. Current Biology, 2017.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC5423359/>

8. Badhiwala, K. N. et al. *Multiple neuronal networks coordinate Hydra mechanosensory behavior*. eLife, 2021.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC8324302/>

9. Lamanna, F. et al. *A lamprey neural cell type atlas illuminates the origins of the vertebrate brain*. Nature Ecology & Evolution, 2023.
   <https://www.nature.com/articles/s41559-023-02170-1>

10. Albuixech-Crespo, B. et al. *Molecular regionalization of the developing amphioxus neural tube challenges major partitions of the vertebrate brain*. PLOS Biology, 2017.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC5396861/>

11. FlyWire Consortium et al. *Neuronal wiring diagram of an adult brain*. Nature, 2024.
    <https://www.nature.com/articles/s41586-024-07558-y>

### Complex systems, emergence, and evolutionary transitions
{: #refs-3 }

12. Simon, H. A. *The Architecture of Complexity*. 1962.
    <https://web.mit.edu/6.033/2006/wwwdocs/papers/protected/simon-complexity.pdf>

13. Anderson, P. W. *More Is Different*. Science, 1972.
    <https://doi.org/10.1126/science.177.4047.393>

14. Maynard Smith, J., & Szathmáry, E. *The major evolutionary transitions*. Nature, 1995.
    <https://www.nature.com/articles/374227a0>

15. West, S. A. et al. *Major evolutionary transitions in individuality*. PNAS, 2015.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC4547252/>

16. *Theoretical foundations of studying criticality in the brain*.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC11117095/>

### Human reasoning, culture, and collective cognition
{: #refs-4 }

17. Sackur, J., & Dehaene, S. *The cognitive architecture for chaining of two mental operations*. Cognition, 2009.
    <https://www.sciencedirect.com/science/article/pii/S0010027709000390>

18. Dehaene, S., & Sigman, M. *From a single decision to a multi-step algorithm*. Current Opinion in Neurobiology, 2012.
    <https://www.sciencedirect.com/science/article/abs/pii/S0959438812000852>

19. Pessoa, L. *On the relationship between emotion and cognition*. Nature Reviews Neuroscience, 2008.
    <https://www.nature.com/articles/nrn2317>

20. Mercier, H., & Sperber, D. *Why do humans reason? Arguments for an argumentative theory*. Behavioral and Brain Sciences, 2011.
    <https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/why-do-humans-reason-arguments-for-an-argumentative-theory/53E3F3180014E80E8BE9FB7A2DD44049>

21. Shea, N. et al. *Supra-personal cognitive control and metacognition*. Trends in Cognitive Sciences, 2014.
    <https://pubmed.ncbi.nlm.nih.gov/24582436/>

22. Hutchins, E. *Cognition in the Wild*. MIT Press, 1995/1996.
    <https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/>

23. Peltokorpi, V., & Hood, A. C. *Communication in Theory and Research on Transactive Memory Systems: A Literature Review*. Topics in Cognitive Science, 2019.
    <https://onlinelibrary.wiley.com/doi/full/10.1111/tops.12359>

24. Heyes, C. *Précis of Cognitive Gadgets: The Cultural Evolution of Thinking*. Behavioral and Brain Sciences, 2018.
    <https://doi.org/10.1017/S0140525X18002145>

25. Muthukrishna, M., & Henrich, J. *Innovation in the collective brain*. Philosophical Transactions of the Royal Society B, 2016.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC4780534/>

26. Ohlsson, S. *Restructuring revisited*. Scandinavian Journal of Psychology, 1984.
    <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9450.1984.tb01005.x>

27. Gentner, D. *Structure-Mapping: A Theoretical Framework for Analogy*. Cognitive Science, 1983.
    <https://www.sciencedirect.com/science/article/abs/pii/S0364021383800093>

### AI, tools, and new representations
{: #refs-5 }

28. LeCun, Y., Bengio, Y., & Hinton, G. *Deep learning*. Nature, 2015.
    <https://www.nature.com/articles/nature14539>

29. Wei, J. et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS, 2022.
    <https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html>

30. Schick, T. et al. *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS, 2023.
    <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>

31. Trinh, T. H. et al. *Solving olympiad geometry without human demonstrations*. Nature, 2024.
    <https://www.nature.com/articles/s41586-023-06747-5>

32. Ellis, K. et al. *DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning*.
    <https://pubmed.ncbi.nlm.nih.gov/37271169/>

33. Fawzi, A. et al. *Discovering faster matrix multiplication algorithms with reinforcement learning*. Nature, 2022.
    <https://www.nature.com/articles/s41586-022-05172-4>

34. Mankowitz, D. J. et al. *Faster sorting algorithms discovered using deep reinforcement learning*. Nature, 2023.
    <https://www.nature.com/articles/s41586-023-06004-9>

35. Romera-Paredes, B. et al. *Mathematical discoveries from program search with large language models*. Nature, 2024.
    <https://www.nature.com/articles/s41586-023-06924-6>

36. Stanford Encyclopedia of Philosophy. *Simplicity*.
    <https://plato.stanford.edu/entries/simplicity/>
