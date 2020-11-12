<?php

namespace Src\More;

use Src\ExtendingClass;

/**
 * This is the DeepClass description.
 */
class DeepClass extends ExtendingClass
{
    /**
     * This is a private method.
     */
    private function thisIsPrivate(): bool
    {
        return true;
    }

    /**
     * This is a public method.
     */
    public function thisIsPublic(): bool
    {
        return true;
    }

    /**
     * This is a protected method.
     */
    protected function thisIsProtected(): bool
    {
        return false;
    }
}