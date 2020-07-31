# diversity-lib
This library's objective is to build a library with all diversity measures proposed in the literature, being it for binary or multi-class problems. Also, we aim to make it accessible for scikit-learn users, making the use of both libraries the easiest as possible.


**Why?**

I'm currently conducting a study and needed to implement the functions for multi-class datasets. Considering that it would take a small amount of time to implement the functions for two-class problems, I decided to do it.

**What diversity measures will be implemented?**

Pairwise:

• Q-statistic;

• The correlation coefficient p;

• Disagreement;

• Agreement;

• Double-fault-measure

For multi-class problems:

• Average Q-statistic;

• Average Disagreement;

• Average Agreement;

• Entropy measure;

• Kohavi-Wolpert Variance;

• Measure of difficulty

All these measures can be found in the following paper: 

Kuncheva, Ludmila I., and Christopher J. Whitaker. "Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy." Machine learning 51.2 (2003): 181-207.

Also, I intend to insert explanations directly on code. 

The coding style will respect the notations used in the article as well (When possible), even though that's not the most pythonic way to implement the functions. 




