<?php

namespace App\Filament\Admin\Resources\WisataResource\Pages;

use App\Filament\Admin\Resources\WisataResource;
use Filament\Actions;
use Filament\Resources\Pages\EditRecord;

class EditWisata extends EditRecord
{
    protected static string $resource = WisataResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\DeleteAction::make(),
        ];
    }
}
