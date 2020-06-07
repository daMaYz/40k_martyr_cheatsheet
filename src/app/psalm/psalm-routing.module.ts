import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PsalmOverviewComponent } from './component/psalmOverview/psalmOverview.component';
import { PsalmDetailComponent } from './component/psalmDetail/psalmDetail.component';
import { DoctrineOverviewComponent } from './component/doctrineOverview/doctrineOverview.component';


const psalmRoutes: Routes = [
    { path: 'overview', component: PsalmOverviewComponent },
    { path: 'detail/:id', component: PsalmDetailComponent, pathMatch: 'full'  },
    { path: 'doctrine/overview', component: DoctrineOverviewComponent },
];

@NgModule( {
    imports: [RouterModule.forChild( psalmRoutes )],
    exports: [RouterModule]
} )
export class PsalmRoutingModule { }
