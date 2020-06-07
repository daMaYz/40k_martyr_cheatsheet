import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

//my
import { PageNotFoundComponent } from './core/component/pagenotfound/pagenotfound.component';
import { WelcomePageComponent } from './core/component/welcomePage/welcomePage.component';

const routes: Routes = [
                        { path: '', component: WelcomePageComponent },
                        { path: 'psalm', loadChildren: () => import( './psalm/psalm.module' ).then( m => m.PsalmModule ) },
                        { path: '**', component: PageNotFoundComponent }
                    ];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    onSameUrlNavigation: 'reload'
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
