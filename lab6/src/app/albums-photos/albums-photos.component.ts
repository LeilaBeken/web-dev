import { Component, OnInit } from '@angular/core';
import { Photos } from '../models';
import { AlbumsService } from '../albums.service';
import {Location} from '@angular/common';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-albums-photos',
  templateUrl: './albums-photos.component.html',
  styleUrls: ['./albums-photos.component.css']
})
export class AlbumsPhotosComponent implements OnInit {
    // @ts-ignore
    album: Album;
    // @ts-ignore
    loaded: boolean;
    photos: Photos[];
  
    constructor(private route: ActivatedRoute,
                private location: Location,
                private albumService: AlbumsService) {
      this.photos = [];
    }
  
    ngOnInit(): void {
      this.getAlbumPhotos();
    }
  
    getAlbumPhotos(): void {
      this.route.paramMap.subscribe((params) => {
        // @ts-ignore
        const id = +params.get('id');
        this.albumService.getAlbumPhotos(id).subscribe((photo) => {
          this.photos = photo;
          this.loaded = true;
        });
      });
    }
  
    goBack(): void {
      this.location.back();
    }
}
