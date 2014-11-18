ButtonHolder();


hole_width = 8;
hole_spread = 20;

module ButtonHolder(height=67,
                    diameter=98.6,
                    outer_thickness=4,
                    inner_thickness=4,
                    inset=17,
                    base_thickness=2)
{
    difference()
    {
        union()
        {
            // Main cylinder body
            cylinder(h=height, d=(diameter + outer_thickness), center=false);

            // base
            translate([0,0,-base_thickness])
            cylinder(h=base_thickness, d=(diameter + outer_thickness), center=false);
        }

        union()
        {
            // Edge for button to sit on
            translate([0,0,height-inset])
            cylinder(h=inset, d=diameter, center=false);
            
            // Main internal cylinder
            cylinder(h=height, d=(diameter - inner_thickness), center=false);

            // Hole for USB
            translate([-90,-6.25,0])
            cube([50, 12.5, 5]);
            
            // Holes for idiocy
            union()
            {
                
                translate([hole_spread,hole_spread,0])
                cylinder(h=10, d=hole_width, center=true);
                
                translate([hole_spread,-hole_spread,0])
                cylinder(h=10, d=hole_width, center=true);
                
                translate([-hole_spread,hole_spread,0])
                cylinder(h=10, d=hole_width, center=true);
                
                translate([-hole_spread,-hole_spread,0])
                cylinder(h=10, d=hole_width, center=true);
            }
        }
    }
}