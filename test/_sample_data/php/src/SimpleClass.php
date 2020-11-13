<?php

namespace Src;

/**
 * This is the description for the SimpleClass.
 * 
 * Here is a more detailed set of detail details for me to
 * detail for you. This is a single paragraph on two lines.
 * 
 * @see ExtendingClass for another example
 * 
 * @method string pretendMethod this method is just a pretend method
 */
class SimpleClass {

    /**
     * @var string $simplePrivateString
     * 
     * This is a simple private string property.
     */
    private $simplePrivateString = 'simple_private_string';

    /**
     * @var string $simpleProtectedString
     * 
     * This is a simple protected string property.
     */
    private $simpleProtectedString = 'simple_protected_string';

    /**
     * @var string $simplePublicString
     * 
     * This is a simple public string property.
     */
    private $simplePublicString = 'simple_public_string';

    /**
     * Simple constructor.
     * 
     * This is a simple constructor's detailed description.
     * 
     * There is more than one paragraph in the detailed description.
     * 
     * @code
     *     $test = 'blah';
     *     $test2 = false;
     * @endcode
     * 
     * @param string $param1 our first parameter.
     * @param array  $param2 our second parameter.
     * @param bool   $param3 out third parameter that has a really long description
     *                       so it must wrap lines.
     */
    public function __construct(string $param1, array $param2 = [], bool $param3 = false)
    {
    }

    /**
     * This method does not have any arguments.
     * 
     * However, we will have a detailed description.
     * 
     * @return string there is a return type
     */
    public function testMethod(): string
    {
        return 'test string';
    }
}