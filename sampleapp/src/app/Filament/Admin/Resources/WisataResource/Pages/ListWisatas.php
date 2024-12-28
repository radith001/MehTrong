<?php

namespace App\Filament\Admin\Resources\WisataResource\Pages;

use App\Filament\Admin\Resources\WisataResource;
use Filament\Actions;
use Filament\Resources\Pages\ListRecords;

class ListWisatas extends ListRecords
{
    protected static string $resource = WisataResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\CreateAction::make(),
        ];
    }
}
