<?php
/*   __________________________________________________
    |  Obfuscated by YAK Pro - Php Obfuscator  2.0.17  |
    |              on 2025-09-17 21:36:03              |
    |    GitHub: https://github.com/pk-fr/yakpro-po    |
    |__________________________________________________|
*/
/*
Art of obfuscation
*/
 namespace App\Models; use Illuminate\Database\Eloquent\Factories\HasFactory; use Illuminate\Foundation\Auth\User as Authenticatable; use Illuminate\Notifications\Notifiable; class User extends Authenticatable { use HasFactory, Notifiable; protected $fillable = ["\x6e\x61\155\x65", "\145\155\x61\x69\x6c", "\160\141\163\x73\167\157\162\x64"]; protected $hidden = ["\x70\141\x73\163\x77\x6f\162\144", "\162\145\155\145\x6d\x62\x65\162\137\x74\x6f\153\145\x6e"]; protected function casts() : array { return ["\x65\155\141\151\154\x5f\166\x65\162\151\x66\x69\x65\x64\137\141\164" => "\144\141\164\x65\164\x69\x6d\x65", "\160\141\163\163\167\157\x72\x64" => "\150\x61\163\150\x65\x64"]; } }
