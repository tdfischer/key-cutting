// Units are in inches, so just multiply everything by the conversion ratio
mm=25.4;

module key() {
	thickness=0.25;
	// Top of loop
	translate([0, 0.5, 0])
		cube([0.25*mm, 0.135*mm, thickness*mm], center=true);

	// Bottom of loop
	translate([0, (0.15625+0.166)*mm, 0])
		cube([0.6*mm, 0.125*mm, thickness*mm], center=true);

	// Left side of loop
	translate([0.16*mm, 0.15*mm, 0])
		rotate([0, 0, 60])
			cube([0.35*mm, 0.125*mm, thickness*mm], center=true);
	// Right side of loop
	translate([-0.16*mm, 0.15*mm, 0])
		rotate([0, 0, -60])
			cube([0.35*mm, 0.125*mm, thickness*mm], center=true);

	// Key head
	translate([0, (0.365+0.1875/2-0.02)*mm, 0]) {
		cube([0.7375*mm, 0.4375*mm, thickness*mm], center=true);
		cube([0.94625*mm, 0.312*mm, thickness*mm], center=true);
		cube([1.01875*mm, 0.1875*mm, thickness*mm], center=true);
	}

	// Key blade
	translate([0, (0.375+1.25/2)*mm, 0])
		cube([0.6025*mm, 1.25*mm, thickness*mm], center=true);

	// Extra width at bottom of jig
	translate([0, (0.875+1.25/2)*mm, 0])
		 cube([0.8*mm, 1.25*mm, 1*mm], center=true);

}

module jigBase() {
		cube([1.75*mm, 1.2*mm, 0.25*mm], center=true);
}

module jigBottom() {
	difference() {
		jigBase();
		translate([0, -9, 0.25*mm-0.06*mm*2]) key();
	}
}

module jigCap() {
	difference() {
		union() {
			cube([1.75*mm-2, 0.25*mm, 0.45*mm-2], center=true);
			for(x = [-1, 1]) {
				translate([(1.75*mm/2-6)*x, 0, -0.45*mm/2+1.5]) cylinder(r=0.35*mm/2, h=0.35*mm, $fn=80);
			}
		}
		translate([0, -9.5, -0.10*mm]) {
			jigBottom();
		}
		translate([0, 0, -0.07*mm]) cube([1*mm, 1*mm, 0.06*mm], center=true);
	}
}

/* translate([0, 1*mm, (0.45*mm-2)/2]) difference() {
	rotate([0, 180, 0]) jigCap();
	for(x = [-1, 1]) {
		translate([(1.75*mm/2-6)*x, 0, -5]) cylinder(r=2.5, h=10, $fn=80);
	}
}*/

translate([0, 0, 0.25*mm]) rotate([0, 180, 0]) {
translate([0, 0, 0.25*mm/2]) difference() {
		jigBottom();
		for(x = [-1, 1], y = [-1, 0, 1]) {
			translate([(1.75*mm/2-6)*x, 9.5+y, -5]) cylinder(r=2.5, h=10, $fn=80);
		}
	}

	translate([0, 0, -0.1*mm]) cube([1.65*mm, 0.25*mm, 0.35*mm], center=true);
}