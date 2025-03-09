# Logarithmic Weighted Random Selector Algorithm: A Novel Approach for Biasing Selection Based on Positional Order Without Hyperparameters

**Iván Alejandro Ramos Herrera**

**[@arhcoder](https://github.com/arhcoder)**

> **First publication:**
> 
> Ramos Herrera, I.A. (2025). *Logarithmic Weighted Random Selector Algorithm: A Novel Approach for Biasing Selection Based on Positional Order Without Hyperparameters*. In: Martínez-Villaseñor, L., Ochoa-Ruiz, G., Montes Rivera, M., Barrón-Estrada, M.L., Acosta-Mesa, H.G. (eds) *Advances in Computational Intelligence. MICAI 2024 International Workshops. MICAI 2024. Lecture Notes in Computer Science*, vol 15464. Springer, Cham. [https://doi.org/10.1007/978-3-031-83879-8_4](https://doi.org/10.1007/978-3-031-83879-8_4)

---

**📄 [Read the Springer paper](https://link.springer.com/chapter/10.1007/978-3-031-83879-8_4 "Springer Nature Link url").**

**📎 Check the [MICAI 2024 slides](https://github.com/arhcoder/LWRS-Algorithm/blob/master/LWRS-MICAI.pdf).**

**🎼 Check the alternative [Project MIA](https://github.com/arhcoder/MIA).**

**⭐ Give a star to [this repository](https://github.com/arhcoder/LWRS-Algorithm "Go and click on the star").**

---

## Abstract

 > The *“Logarithmic Weighted Random Selector”* (LWRS) introduces a novel algorithm designed for selecting randomly one item from a list, with the bias that the further to the beginning of the list each one is, the more likely it is to be selected. Unlike traditional selection and sampling methods that rely on numerical fitness scores or require hyperparameter tuning, LWRS employs a logarithmic weighting mechanism to naturally favor items based on their position. It arose from the problem of requiring a method that allows weighting a selection based on the order of preference on a list of elements, for phenomena for which numerical weighting values ​​are unknown but only their order, which unlike algorithms such as *Rank-based Selection*, does not require configuration of hyperparameters. Different mechanisms were explored, such as a *Linear Selection* method and *Exponential Selection*. Discovering that utilizing a logarithmic scale, LWRS achieves a non-numerical preference bias, distinguishing itself from classic methods of weighted random sampling as *Fitness-proportionate selection* and *Tournament Selection*, which do require defined numerical weights, contributing to the field with a straightforward, parameter-free approach to weighted random selection.

---

## Application
In the following video it is an application of the algorithm, not included in the paper. In this one, the melody ***"Aria di Mezzo Carattere"*** composed by *Nobuo Uematsu* for *Final Fantasy VI* game was taken, and the algorithm was used to decide which notes to use to replace in the melody.

To decide each note, the list with the musical notes ordered by hierarchy was passed to the **LWRS** decision algorithm, where preference was given to:
1. Notes that belong to the chord.
2. Notes that belong to the tonality.
3. Notes that do not belong to the tonality.
Also ordering the notes by their proximity to the first note chosen (chosen only from the notes of the initial chord).

In this way, three melodies were obtained that were different from the original, which, during the presentation of the work for the ***Mexican International Congress of Artificial Intelligence (MICAI) 2024***, at the ***National Institute of Astrophysics, Optics and Electronics (INAOE)***, on October 21 at *Tonantzintla, Puebla*, were presented to the public present, obtaining answers to the questions:

1. **Which melody did you like the most?**
2. **Which do you think is the original version?**

With the following statistics:

*[Missing data :c]*.

[![MICA Video](https://raw.githubusercontent.com/arhcoder/LWRS-Algorithm/Images/master/LWRS-MICAI.png)](https://raw.githubusercontent.com/arhcoder/LWRS-Algorithm/master/LWRS-MUSIC.mp4)

This application demonstrated that the algorithm can function as a note selector in a melody, based on basic rules of tonal music hierarchy, without the need to provide extra hyperparameters and achieving results as good as those composed by a person.

---

## Why?
Traditional selection methods in evolutionary computing —such as *fitness-proportionate* or *tournament selection*— requires numerical fitness values or hyperparameter configuration to bias choices. **LWRS** addresses scenarios in which the importance of options is determined solely by their ranking in a list. Motivated by challenges in generative models (for example, simulating music composition where stylistic patterns prevail without explicit numerical scores), **LWRS** provides a straightforward solution to achieve selection bias based solely on positional order.

This algorithm was born out of the need for the generative music algorithm **MIA**, which is not trained with real music instances and instead needs to make musical aesthetic decisions based on style preferences or hierarchy rules that, when making random decisions, not only mostly converge to certain preferable decisions in this hierarchy, but also leave room for any other to appear. **[Check out the MIA PROJECT here](https://github.com/arhcoder/MIA).**

---

## Formulation

To construct a logarithmic scale that adapts to the number of objects ($n$) in a list, **LWRS** simulates a set $\mathbb{P}$ of points on a Cartesian axis. Each point defines the boundary of a sector corresponding to one object. The scale is constructed using the following set definition:

$$
\mathbb{P} = \{ p_i : p_i = \bigl(n \cdot \log_{n+1}(i+1),\ 0\bigr),\ i \in \mathbb{N},\ 1 \leq i \leq n \}
$$

Where:

- $p_i$ is the coordinate $(x,y)$ of the $i$-th point.
- $n$ is the total number of objects.
- $i$ is the index of the point, with $1 \leq i \leq n$.

The $x$-coordinate of each point represents the cumulative distance from the origin along the logarithmic scale. Thus, the distance $d_i$ from the origin $(0,0)$ to the $i$-th point is given by:

$$
d_i = n \cdot \log_{n+1}(i+1)
$$

### Example: $n = 5$

Consider a list of 5 objects, where the position in the list indicates the preferencea and where being the first one the most favored. The scale is divided into 5 sectors, and the division points are calculated as follows:

**For $i=1$ ⮕** $p_1 = \Bigl( 5 \cdot \log_{6}(1+1),\ 0 \Bigr) \approx (1.934,\, 0)$

**For $i=2$ ⮕** $p_2 = \Bigl( 5 \cdot \log_{6}(2+1),\ 0 \Bigr) \approx (3.066,\, 0)$

**For $i=3$ ⮕** $p_3 = \Bigl( 5 \cdot \log_{6}(3+1),\ 0 \Bigr) \approx (3.869,\, 0)$

**For $i=4$ ⮕** $p_4 = \Bigl( 5 \cdot \log_{6}(4+1),\ 0 \Bigr) \approx (4.491,\, 0)$

**For $i=5$ ⮕** $p_5 = \Bigl( 5 \cdot \log_{6}(5+1),\ 0 \Bigr) = (5,\, 0)$

These calculations partition the total scale into 5 sectors, where each sector's boundary is determined by the corresponding distance $d_i$.

![Figure 1. Five spaces logarithmic scale graphing](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/log5.png?raw=true)

**Figure 1.** *Five spaces Logarithmic scale graphing.*

---

## LWRS Algorithm
```python
def lwrs(objects):
    n = len(objects)
    
    if n == 0:
        return "No objects"
    if n == 1:
        return objects[0]
    
    random_point = random.uniform(0, n)
    for i in range(1, n + 1):
        if random_point <= n * math.log(i+1, n+1):
            return objects[i-1]
```

This code details the core operation: generating a random point and iterating through the logarithmically determined boundaries to select the corresponding object.

---

## Experiments

To assess the bias introduced by **LWRS**, a series of experiments were performed by repeatedly executing the selection process and recording how frequently each object was chosen. The frequency counts were then plotted to visualize the selection distribution. For instance, when running the algorithm with different list sizes and iteration counts, the following observations were made:


![Figure 2. Experiment with 5 objects over 100 iterations.](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/exp1.png?raw=true)
**Figure 2.** *Experiment with 5 objects over 100 iterations*.

![Figure 3. Experiment with 10 objects over 100,000 iterations](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/exp2.png?raw=true)
**Figure 3.** *Experiment with 10 objects over 100,000 iterations*.

![Figure 4. Experiment with 20 objects over 10,000,000 iterations](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/exp3.png?raw=true)
**Figure 4.** *Experiment with 20 objects over 10,000,000 iterations*.

These plots clearly show a logarithmic decay pattern: objects at the top of the list are selected significantly more often than those near the end. This confirms that **LWRS** effectively biases the selection based solely on positional order without requiring any hyperparameters.

---

## Alternatives

While LWRS offers a parameter-free approach to biasing selections, two other methods based on item order are noteworthy:

### 1. Linear Weighted Selection

In the linear approach, each object is assigned a weight inversely proportional to its position in the list. For a list with $n$ objects, the weight for the $i$-th object is given by:

$$
w_i = n - i + 1
$$

The probability of selecting the $i$-th object is then:

$$
p_i = \frac{w_i}{\sum_{j=1}^{n} w_j}
$$

The pseudocode for this method is:

```plaintext
Algorithm: linear(objects)
1. n ← length(objects)
2. weights ← [n, n-1, ..., 1]
3. total ← sum(weights)
4. probabilities ← [w/total for w in weights]
5. random_value ← random(0, n)
6. cumulative ← 0
7. for i from 1 to n do
8.     cumulative ← cumulative + probabilities[i]
9.     if cumulative ≥ random_value then
10.         return objects[i]
```

### 2. Exponential Weighted Selection

This method builds on the linear approach by raising each weight to a power $x$, thereby intensifying the bias towards top-ranked elements. The probability is calculated as:

$$
p_i = \frac{(w_i)^x}{\sum_{j=1}^{n} (w_j)^x}
$$

where $x$ is a chosen exponent. The corresponding pseudocode is:

```plaintext
Algorithm: exponential(objects, x)
1. n ← length(objects)
2. weights ← [n, n-1, ..., 1]
3. weights ← [w^x for w in weights]
4. total ← sum(weights)
5. probabilities ← [w/total for w in weights]
6. random_value ← random(0, n)
7. cumulative ← 0
8. for i from 1 to n do
9.     cumulative ← cumulative + probabilities[i]
10.    if cumulative ≥ random_value then
11.         return objects[i]
```

**Figure 5** illustrates how varying the exponent $x$ affects the selection bias. With $x=1$, the method reduces to the linear case, while higher values of $x$ progressively increase the preference for items at the top of the list.

![Figure 5: Effect of different exponent values on Exponential Weighted Selection (with $x=1$ representing the linear case)](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/exponential.png?raw=true)

---

## Comparison

A comparative evaluation of the selection methods —including *Simple Random Sampling*, *Linear Weighted Selection*, *Exponential Weighted Selection*, and **LWRS**— is summarized in **Figure 6**.

![Figure 6: Comparison between selection algorithms](https://github.com/arhcoder/LWRS-Algorithm/blob/master/Images/comparison.png?raw=true)

---

## Contact and Contributions
For further information or to contribute to the project, please contact:  
**Iván Alejandro Ramos Herrera** – **[arhcoder@gmail.com](mailto:arhcoder@gmail.com)**

Contributions, collaborations, and constructive feedback are warmly welcome in **[this repository](https://github.com/arhcoder/LWRS-Algorithm).**

---