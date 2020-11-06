<?php

namespace Src\More;

/**
 * This trait is used by the DeepClass.
 * 
 * The requiredMethod is provided to satisfy DeepInterface
 * 
 * @see Src\More\DeepInterface
 * @see Src\More\DeepClass
 */
trait DeepTrait
{
    /**
     * This method is required by this interface.
     * 
     * Our method definition will override the interface's definition.
     * 
     * @param int    $param1 this is parameter 1
     * @param string $param2 this is parameter 2
     * 
     * @return array the returned array
     */
    public function requiredMethod(int $param1, string $param2): array
    {
        return [];
    }

    /**
     * @inheritdoc
     */
    public function requiredMethod2(int $param1): bool
    {
        return false;
    }

    /**
     * {@inheritdoc}
     * 
     * @param int $param1 this documentation should be overridden
     * 
     * @return bool this should be overridden
     */
    public function requiredMethod3(int $param1): bool
    {
        return false;
    }

    /**
     * This method is not required.
     * 
     * @return bool the returned bool
     */
    public function unrequiredMethod(): bool
    {
        return false;
    }
}