const navSlide = () => {
	const navbar = document.querySelector('.navbarsicon');
	const navlink = document.querySelector('.navlinkul');
	const navlinks = document.querySelectorAll('.navlinkul li');

	navbar.addEventListener('click', ()=>{
        navlink.classList.toggle('nav-active');
	});

	navlinks.forEach((link, index)=>{
        link.style.animation = 'NavLinkFade 0.5s easy forwards ${index / 7 + 2}s';

	});
}

navSlide();