const sublinks = document.getElementsByClassName('sublinks');
const tabcontents = document.getElementsByClassName('tabcontents');

// Loop through sublinks and add event listeners
for (let i = 0; i < sublinks.length; i++) {
  sublinks[i].addEventListener('click', () => {
    // Remove active class from all sublinks
    for (let j = 0; j < sublinks.length; j++) {
      sublinks[j].classList.remove('activelink');
    }
    // Add active class to the current sublink
    sublinks[i].classList.add('activelink');
    
    // Remove active class from all tab contents
    for (let k = 0; k < tabcontents.length; k++) {
      tabcontents[k].classList.remove('activetab');
    }
    // Add active class to the tab content matching the sublink
    if (tabcontents[i]) {
      tabcontents[i].classList.add('activetab');
    }
  });
}