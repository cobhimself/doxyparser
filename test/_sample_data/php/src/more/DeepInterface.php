<?php

namespace Src\More;

/**
 * This interface is used by the DeepClass.
 * 
 * The requiredMethod will be provided by a trait though.
 * 
 * @see DeepClass
 */
interface DeepInterface
{
    /**
     * This method is required by this interface.
     * 
     * @see DeepTrait for how it is implemented.
     * 
     * @param int    $param1 this is parameter 1
     * @param string $param2 this is parameter 2
     * 
     * @return array the returned array
     */
    public function requiredMethod(int $param1, string $param2): array;

    /**
     * We will inherit this method's documentation.
     * 
     * @param int $param1 the first parameter
     * 
     * @return bool the returned bool
     */
    public function requiredMethod2(int $param1): bool;

    /**
     * We will inherit this method's documentation but differently.
     * 
     * @param int $param1 the first parameter
     * 
     * @return bool the returned bool
     */
    public function requiredMethod3(int $param1): bool;
}