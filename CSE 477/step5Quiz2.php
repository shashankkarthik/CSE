<?php

class QuadraticTest extends \PHPUnit_Framework_TestCase {
    
    public function test_roots() {
        //Check Null A
        $a = null;
        $b = 2;
        $c = -3;
        $quad = new Quadratic($a, $b, $c);  
        $this->assertEquals(null, $quad->roots());
        
        //Check Negative Rad
        $a = 2;
        $b = 1;
        $c = 1;
        $quad = new Quadratic($a, $b, $c);
        $this->assertEquals(null, $quad->roots());
        
        //Test valid quadratic
        $a = 1;
        $b = 2;
        $c = -3;
        $quad = new Quadratic($a, $b, $c);
        $roots = $quad->roots();
        
        $this->assertEquals(-3,$roots[0],"Should be -3", 0.001);
        $this->assertEquals(1,$roots[1],"Should be 1", 0.001);
        
    }
    
    public function test_equationHTML() {
        //Test Null Roots
        $a = 1;
        $b = 2;
        $c = 3;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("has no roots.",$quad->rootsHtml());
        
        //Test Good roots with abc vals
        $a = 1;
        $b = 2;
        $c = -3;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("The roots of x<sup>2</sup> + 2x - 3 are -3 and 1",$quad->rootsHtml());
        
        //Test Good roots with positve a, neg b, neg c
        $a = 1;
        $b = -2;
        $c = -3;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("The roots of x<sup>2</sup> - 2x - 3 are -1 and 3",$quad->rootsHtml());
        
        //Test good roots with ab vals
        $a = -1;
        $b = 1;
        $c = 0;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("The roots of -x<sup>2</sup> + x are 1 and 0",$quad->rootsHtml());
               
        //Test good roots with ac vals
        $a = 1;
        $b = 0;
        $c = -1;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("The roots of x<sup>2</sup> - 1 are -1 and 1.",$quad->rootsHtml());
        
        
        //Test bad roots with ac vals
        $a = 1;
        $b = 0;
        $c = 1;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("x<sup>2</sup> + 1 has no roots.",$quad->rootsHtml());
        
        
        //Test bad roots with bc vals
        $a = 0;
        $b = 1;
        $c = 1;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("x + 1 has no roots.", $quad->rootsHtml());  
        
        //Test only c val
        $a = 0;
        $b = 0;
        $c = 1;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("1 has no roots.", $quad->rootsHtml());
        
        //Test only a val
        $a = 3;
        $b = 0;
        $c = 0;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("The roots of 3x<sup>2</sup> are 0 and 0.", $quad->rootsHTML());
        
        //Test only b val
        $a = 0;
        $b = -1;
        $c = 0;
        $quad = new Quadratic($a, $b, $c);
        $this->assertContains("-x has no roots.", $quad->rootsHtml());
    }

}