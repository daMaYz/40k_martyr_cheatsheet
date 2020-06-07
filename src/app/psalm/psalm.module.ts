import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FieldsetModule } from 'primeng/fieldset';
import { FormsModule } from '@angular/forms';
import { TableModule } from 'primeng/table';

//my
import { PsalmRoutingModule } from './psalm-routing.module';
import { PsalmContainerComponent } from './component/psalmContainer/psalmContainer.component';
import { PsalmOverviewComponent } from './component/psalmOverview/psalmOverview.component';
import { PsalmDetailComponent } from './component/psalmDetail/psalmDetail.component';
import { DoctrineOverviewComponent } from './component/doctrineOverview/doctrineOverview.component';

@NgModule( {
    imports: [
        CommonModule,
        FieldsetModule,
        FormsModule,
        TableModule,
        
        PsalmRoutingModule,
    ],
    declarations: [
        PsalmContainerComponent,
        PsalmOverviewComponent,
        PsalmDetailComponent,
        DoctrineOverviewComponent,
    ],
    exports: [
        CommonModule,
        PsalmContainerComponent,
        PsalmOverviewComponent,
        PsalmDetailComponent,
        DoctrineOverviewComponent,
    ],
    providers: []
} )
export class PsalmModule { }
