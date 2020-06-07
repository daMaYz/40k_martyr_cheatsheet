import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component( {
    selector: 'pagenotfound',
    templateUrl: './pagenotfound.component.html'
} )
export class PageNotFoundComponent implements OnInit {


    constructor(private router: Router) { }

    ngOnInit(): void {
        console.log('redirectTo: ', this.router.url);
        this.router.navigate([this.router.url]);
    }
}
