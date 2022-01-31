#!/usr/bin/env python
# coding: utf-8

# # Implementation of a stopwatch with LCD display
# ## Laboratory Class 04 - 12 October 2021
# 
# ### Topics
# - Finite-state machines.
# - Basic hardware circuits:
#     - data latches.
# - Verilog programming language:
#     - peripheral device drivers (ex.gr.: LCD driver with display of the lap mode).
# 
# ## Problems:
# - implementation of a synchronous 5-state finite-state machine with two pulse control;
# - final implementation of a stopwatch with 1/100 s resolution, start/stop, lap/reset function, and LCD display.
# 
# ---
# 
# ## Finite-state machines
# 
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Finite-state_machine)
# A finite-state machine (FSM) or finite-state automaton (FSA, plural: automata), finite automaton, or simply a state machine, is a mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one state to another in response to some inputs; the change from one state to another is called a transition. An FSM is defined by a list of its states, its initial state, and the inputs that trigger each transition. Finite-state machines are of two types—deterministic finite-state machines and non-deterministic finite-state machines. A deterministic finite-state machine can be constructed equivalent to any non-deterministic one.
# ```
# Despite the long mathematical definition state machines are simpler than first expected. They just define how to switch from a state to an other depending on an event. Let's make and example with a well know state machine: Pac Man's ghosts:
# ![](https://miro.medium.com/max/1400/0*rVk-GYIMZJMD8Lxd)
# 
# The image taken from [a medium article](https://mark-truluck.medium.com/the-machine-in-the-ghost-46f856f94ed2) explains the behaviour of the ghosts with states and how they transition from one state to an other accordin to events.
# 
# States machines can be easily implemented with ```if-else```, ```switch``` construct and ```enums```. Each case correspond to a state and the condition to the event.
# 
# ### Clocks
# Finite state machines can even be use to generate a clock with an arbitrary frequence. Assume we want to count $n$ ticks of a given clock. In that case it is possible to consider $n$ states and as many transitions. A transition will occur at each tick of the given clock.
# ![Representation of a clock as a FSM](./images/21-10-12-FSM-clock.jpg)
# 
# <!-- add image -->
# 
# ### Gray 
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Gray_code)
# The reflected binary code (RBC), also known as Gray code, is an ordering of the binary numeral system such that two successive values differ in only one bit (binary digit).
# For example, the representation of the decimal value "1" in binary would normally be "001" and "2" would be "010". In Gray code, these values are represented as "001" and "011". That way, incrementing a value from 1 to 2 requires only one bit to change, instead of two.
# Gray codes are widely used to prevent spurious output from electromechanical switches and to facilitate error correction in digital communications such as digital terrestrial television and some cable TV systems.
# ```
# <!-- [A simulation on falstad](https://www.falstad.com/circuit/e-graycode.html) -->
# 
# ## Data Latches
# A data latch is just a way to use D Flip-Flops to store data. Usually a data latch (or register) will store a new value only on a positive edge and will preserve the old value otherwise.
