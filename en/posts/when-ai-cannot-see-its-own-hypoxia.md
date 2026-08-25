---
layout: post
title: "When a System Cannot See Its Own Hypoxia: From AI Agents and Automation to Institutional Design"
date: 2026-08-25 15:20:00 +0800
lang: en
permalink: /en/posts/when-ai-cannot-see-its-own-hypoxia/
alternate_url: /posts/when-ai-cannot-see-its-own-hypoxia/
categories: [AI, System Design]
tags: [AI Agent, Automation, Control Systems, AI Governance]
description: "An Agent should not replace automation—but placing an Agent above automation is still not enough. A mature system must be able to discover its own blind spots and externalize safety into independent oversight, separation of authority, and institutions."
toc: true
comments: true
---

Freediving presents a danger that systems designers should find especially interesting: a person can lose consciousness from hypoxia without first receiving a sufficiently urgent subjective warning.

Much of the urge to breathe comes from the accumulation of carbon dioxide. Hyperventilating before a dive lowers carbon dioxide and delays the feeling that one must breathe, without producing a proportional increase in the oxygen available to the body. The alarm can therefore grow quieter while the underlying danger continues to approach. Medical literature calls this kind of underwater loss of consciousness a hypoxic blackout. It is a stark reminder that an absent warning is not the same thing as an absent danger. The [NCBI Bookshelf overview](https://www.ncbi.nlm.nih.gov/books/NBK554620/) provides a concise account of the physiology.

The human response to this problem is revealing. We do not demand that a diver “be more rational” after consciousness is already gone. Nor do we expect the existing respiratory reflex to suddenly learn every exceptional condition. Instead, we understand the blind spot in our internal warning system and build mechanisms outside the body: do not dive alone; have a buddy observe from a different state; agree on monitoring and rescue procedures in advance; turn accumulated experience into training and rules.

That changed how I think about AI Agents and automation.

## An Agent should not replace automation

My starting point was that an Agent does not replace automation. It replaces the person who used to stand above automation—to operate it, interpret what it was doing, intervene when necessary, and improve it over time.

Automation is well suited to work that is known, repetitive, and explicitly specifiable. It is fast, inexpensive, stable, testable, and comparatively easy to audit. An Agent is better suited to situations the rules do not cover: interpreting a goal, resolving ambiguity, negotiating conflicts, planning across a longer horizon, or finding a new recovery path after a workflow fails.

The sensible execution path is not to send every event through an LLM:

```text
Normal case
Event → Automation → Action

Novelty or exception
Event → Automation → Escalation → Agent
```

This distinction matters. If an LLM timeout stops an entire production workflow, the result is not an autonomous system. It is a single point of failure that happens to be better at conversation.

An Agent is therefore closer to a supervisory controller. It does not need to reimplement the lower-level process. It determines the context, objective, threshold, parameters, priority, and resource budget under which automation operates. When the same exception appears repeatedly, the Agent should also turn a validated response into new automation so that the next occurrence does not require the same reasoning again.

## The body is not a hierarchy in which the brain commands everything

The nervous system pushes this model one step further.

The spinal cord and brainstem handle fast, continuous, survival-critical control. The cerebellum corrects movement through error signals and helps produce fluent skills. The cerebral cortex is particularly good at novel, abstract, and longer-horizon problems. Once the thalamus, basal ganglia, hypothalamus, hippocampus, amygdala, autonomic nervous system, and endocrine system enter the picture, the body no longer looks like a system with one central Agent.

It looks more like a collaboration among specialized closed loops. Some route information. Some retain contextual memory. Some select one action while suppressing its competitors. Some rapidly assess threat. Some maintain internal homeostasis. Some complete an entire sensor–controller–actuator loop locally.

Mapped into software, the rough outline becomes:

```text
Memory ↔ Router ↔ Agent ↔ Action Gate
              ↕          ↕
          Risk Layer   Learner
              ↕          ↕
          Local Automation
                 ↕
             Environment

Homeostasis and global state modulate every level
```

In this model, the Agent is no longer the mandatory route for every piece of information and every action. It specializes in the parts the system has not yet learned. Known problems go to automation; local errors are corrected by local controllers; only high prediction error, conflicting objectives, or genuinely unfamiliar situations escalate upward.

This changes the standard by which an Agent should be judged. A good Agent does not merely complete today’s task. It makes tomorrow’s version of the same task progressively less dependent on the Agent.

## Multiple closed loops can still be wrong together

At this point the model can appear complete: sensing, memory, routing, risk, learning, homeostasis, and high-level reasoning all have their place. The freediving example exposes a deeper problem.

A controller never has direct access to “the true state itself.” It has access to sensor readings and proxies:

```text
True state
   ↓  not necessarily observable
Sensors and proxies
   ↓
The controller's judgement
   ↓
Action
```

Whenever a proxy loses its relationship to the state it is meant to represent, a closed loop can remain internally coherent while becoming externally wrong.

Software is full of these cases. An API reports success while the data is already corrupted. Every test passes because the tests omit the actual risk. A dashboard stays green because its monitoring feed stopped updating. A model reports high confidence on an input that lies outside its range of competence. Worse, several controllers that share the same data, model, and assumptions may not correct one another. They may fail together.

Adding “another Agent to supervise” does not automatically create safety. If two Agents use the same model, read the same data, depend on the same service, and share the same authority, they resemble two divers descending at the same time: there are now two people, but no independent capacity for rescue.

## The value of reason is its ability to move protection outside itself

Freediving offers more than an analogy for the nervous system. It also shows where that analogy ends.

Humans can understand that their sensors may mislead them. We can reason that once consciousness is lost, self-correction is no longer available. We can then redesign the activity itself: who observes whom, who is allowed to do what, and who takes over when the original controller fails.

Learning can be divided into three levels:

```text
Parameter adaptation
Adjust thresholds, weights, and policies inside an existing architecture

Architectural adaptation
Discover a structural blind spot, then add sensors or change control relations

Institutional adaptation
Externalize the new understanding into roles, authority, procedures,
review, and shared memory
```

The last level is crucial. Individual understanding disappears with the individual. An institution can allow people who have never personally encountered the accident to follow rules learned from it. Human capability therefore resides not only in brains, but also in instruments, language, partners, operating procedures, scientific literature, and institutions.

## Software systems also need a “dive buddy”

A software dive buddy should fail under different conditions from the primary system. It need not be more intelligent than the main Agent, but it must possess enough independence to remain useful:

- Observe through different data sources rather than rereading the same output.
- Operate in a separate execution environment where appropriate.
- Hold the minimum authority required to stop or isolate the primary system.
- Remain outside the main Agent’s unilateral power to disable or rewrite.
- Separate proposal, approval, and execution for high-risk actions.
- Preserve audit records that the actor cannot overwrite.
- Use canaries, fault injection, and exercises to test whether safeguards actually work.
- Monitor not only the business metric, but whether monitoring itself remains alive.

The common purpose of these measures is to reduce common-mode failure: do not allow every protective layer to fail for the same reason.

This also explains why governance cannot be an approval button attached at the very end. It must run through design, testing, deployment, monitoring, and retirement. Independent review is valuable precisely because it can expose internal blind spots and conflicts of interest. This is broadly consistent with the [NIST AI Risk Management Framework](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), which treats governance as continuous and emphasizes defined responsibilities, testing and validation, and independent assessment.

## The Agent's highest-level job is to participate in mechanism design

If an Agent can only handle exceptions inside a workflow, it remains a more flexible operator. A more capable Agent should be able to ask a different class of question:

- Under what conditions does the metric we rely on stop representing reality?
- Which important states are not observed at all?
- If the Agent itself fails, who or what can notice?
- Which safeguards secretly share the same failure source?
- Which operations should not be proposed, approved, and executed by the same actor?
- Which lessons from incidents have not yet become durable rules?

From incidents, near misses, and counterfactual simulation, an Agent could propose new sensors, separation of authority, cross-checks, operating procedures, or safety boundaries. It should not, however, be able to rewrite its own highest constraints unilaterally.

A safer path is:

```text
The Agent discovers a risk
      ↓
Builds a causal and failure model
      ↓
Proposes a new external mechanism
      ↓
Simulation, testing, and fault injection
      ↓
Independent review / human governance
      ↓
Staged deployment
      ↓
The mechanism becomes a new institutional and safety boundary
```

The Agent can participate in institutional evolution. It should not simultaneously be the proposer, approver, executor, and final supervisor.

## From one Agent to a system that can see its own boundaries

A mature intelligent automation system therefore needs at least five levels:

```text
Institutions and external governance
Separation of roles, independent oversight, standards, and shared memory
              ↕
Meta-control / Mechanism Design
Discover blind spots, model failures, redesign the architecture
              ↕
Agent / Higher cognition
Novel problems, causal understanding, reasoning, and long-horizon planning
              ↕
Specialized control and adaptation
Memory, routing, risk, arbitration, learning, and homeostasis
              ↕
Automation / Local Control
Fast, reliable, testable handling of known cases
              ↕
Environment
```

Automation handles the known. Local controllers handle immediate feedback. Learners turn experience into skill. The Agent handles novelty the system has not yet absorbed. Meta-control studies how the control architecture itself can fail. Institutions and external governance provide independent protection when the primary system is impaired and preserve knowledge beyond the lifetime of any one Agent.

What is worth imitating, then, is not only the brain, nor even the nervous system as a whole. It is the way humans use reason to understand their own limitations, then use tools, cooperation, science, and institutions to compensate for them.

A mature Agent system does more than act on its environment, and more than tune its automation. It must also know that what it sees is not the world itself; that its alarms can fall silent; that its judgement can fail—and, while it can still reason, place the necessary protection outside itself.
