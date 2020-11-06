<?php

namespace Src;

use SimpleClass;

/**
 * This class extends the SimpleClass.
 */
class ExtendingClass extends SimpleClass
{

    /**
     * This method is an additional one.
     * 
     * @param string $test this is a test argument
     * 
     * @return array this is the returned array description
     */
    public function additionalMethod(string $test = 'test'): array
    {
        return [];
    }
}