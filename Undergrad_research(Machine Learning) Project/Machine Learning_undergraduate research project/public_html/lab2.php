<?php include("/export/home/fri/public_html/common/header.php"); ?>

<h2>Andrew Kim's Lab2 Assignment</h2>
       
<div class="text"> 

<!-- Type below here! -->

<ol>
    <li>In two classes of generating Potential Energy Surfaces(PES), there exists Empiricial Potentials(Force Fields) and Electronic Structure Methods.
        Empricial Potentials use when the experiment needs less accuracy, cannot afford electronic structure calculations, and explores computational methods and a well studied system.
        In contrast, Electronic Structure Methods use when the experiment needs the accuracy, can afford electronic structure calculations, and creates application projets such as discovering new materials or comparing computational results with experimental results.
        In reference, Lennard-Jones belongs Empirical Potentials class. </li>
    <li>Epsilon(e) means the well depth and a measure of how strongly the two particles attract each other. Sigma(σ) is the distance at which the intermolecular potential between the two particles is zero. It gives a measurement of how close two non-bonding particles can get and is thus referred to as the van der Waals radius.
        Specifically, when the bonding potential energy is equal to zero, the distance of separation(r) will be equal to σ.
        σ is equal to one-half of the internuclear distance between nonbonding particles.
        <img src = "Lennard-Jones Potential.png"> <a href = "https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Intermolecular_Forces/Specific_Interactions/Lennard-Jones_Potential">Source</a> </li>
    <li>The optimal distance(bond length) is 1.222 between two atoms in the 
        L-J potential(epsilon = 1.0, sigma = 1.0). The equation is based on
        r(n+1) = r(n) + aF(r(n)). To refer results, link the txt file about
        results when alpha changed.
        <a href = "LJ Potential result.txt">Result</a>
        </li>
    <li>To observe the results, the final potential energy, force and final bondlength
        is closed to -1, 0, and 1.222 each. However, the difference of changing alpha
        is the number of steps. I will choose alpha 0.003(low value). Above the result of textfile, when the value of alpha increases, the step also increases.
        I think the less step, the more efficient to find optimal distance. Below the links, we could see all the process.        
        <a href = "/export/home/fri/akim/lab2-part2/stepBoLen_alpha0.001.png">Bond length(a = 0.001)</a>
        <a href = "stepBoLen_alpha0.003.png">Bond length(a = 0.003)</a>
        <a href = "../lab2-part2/stepBoLen_alpha0.005.png">Bond length(a = 0.005)</a>
        <a href = "../lab2-part2/stepBoLen_alpha0.007.png">Bond length(a = 0.007)</a>
        <a href = "../lab2-part2/stepBoLen_alpha0.009.png">Bond length(a = 0.009)</a>
        



    </li>
</ol>










<!-- And above here -->

</div>

<?php include("/export/home/fri/public_html/common/footer.php"); ?>

